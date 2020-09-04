import pandas
from dataclasses import dataclass
from .database.Database import Database

from models.DataDW import DataDWFields, DWTables
from helpers.decoder import decode
from helpers.join import join

from load.repositories.LocationsRepository import LocationsRepository
from load.repositories.GranularitiesRepository import GranularitiesRepository
from load.repositories.ReferencePeriodRepository import ReferencePeriodRepository
from load.repositories.InformationsRepository import InformationsRepository
from load.repositories.DataTypesRepository import DataTypesRepository

from load.repositories.Repository import Repository
from .Mapper import Mapper


@dataclass
class Load:
    database: Database
    periode_summed_series: pandas.Series

    _data_dw_df: pandas.DataFrame = pandas.DataFrame([])

    def start(self):
        self.database.start_connection()

        repository = Repository(database=self.database)

        locations = LocationsRepository(repository).fetch_locations()

        granularities = GranularitiesRepository(
            repository).fetch_granularities()

        rf_periods = ReferencePeriodRepository(
            repository).fetch_reference_periods()

        info = InformationsRepository(repository).fetch_informations()

        dt_type = DataTypesRepository(repository).fetch_data_types()

        self.fill_all_data_dw_fields(
            locations, granularities, rf_periods, info, dt_type)

    def end(self):
        self.database.close_connection()

    def create_insert_query(self, row):
        fields_list = [
            DataDWFields.DATA,
            DataDWFields.INFORMATION,
            DataDWFields.DATA_TYPE,
            DataDWFields.REFERENCE_PERIOD,
            DataDWFields.LOCATION,
            DataDWFields.GRANULARITY,
        ]

        id_list = [
            str(row[field]) if field == DataDWFields.DATA else str(
                int(row[field]))
            for field in fields_list
        ]

        query = f"INSERT INTO {DWTables.DATA}"
        query += f"({join(fields_list)})"
        query += f" VALUES ({join(id_list)})"

        print(query)
        return query

    def fill_all_data_dw_fields(self, locations, granularities, rf_periods, info, dt_type):
        mapper = Mapper(locations, granularities, rf_periods, info, dt_type)

        actions = {
            DataDWFields.LOCATION: lambda period: mapper.city_name_to_id(period.city_name),
            DataDWFields.GRANULARITY: lambda period: mapper.period_name_to_id(period.periode),
            DataDWFields.REFERENCE_PERIOD: lambda period: mapper.reference_period_to_id(period.reference_periode),
            DataDWFields.INFORMATION: lambda period: mapper.get_information_id(),
            DataDWFields.DATA_TYPE: lambda period: mapper.get_data_type_id(),
            DataDWFields.DATA: lambda period: period.value
        }

        for field, function in actions.items():
            self._data_dw_df[field] = self.periode_summed_series.apply(
                function)

        df = self._data_dw_df

        for _, row in df.iterrows():
            self.create_insert_query(row)
