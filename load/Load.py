import pandas
from dataclasses import dataclass
from .database.Database import Database

from unidecode import unidecode
from models.DataDW import DataDWFields, DWTables
from .Mapper import Mapper


def get_location_dict():
    file_path = "load/ibge.csv"
    encode = "windows-1252"
    df = pandas.read_csv(
        filepath_or_buffer=file_path,
        encoding=encode,
        sep=";",
        usecols=[2, 3],
    )

    MUN = 'Município-UF'
    IBGE = 'IBGE'

    locations = {
        unidecode(row[MUN]): row[IBGE]
        for _, row in df.iterrows()
    }

    return locations


@dataclass
class Load:
    database: Database
    periode_summed_series: pandas.Series

    _data_dw_df: pandas.DataFrame = pandas.DataFrame([])

    def start(self):
        self.database.start_connection()

        '''
        qr_locations = self.database.execute_query(
            'SELECT `name`, `id_ibge` FROM `Location`')
        '''

        def query(query): return self.database.execute_query(query)

        qr_granularity = query(
            f'SELECT `id`, `granularity` FROM `{DWTables.GRANULARITY}`')

        qr_rf_periods = query(
            f'SELECT `id`, `in_date`, `until_date` FROM `{DWTables.REFERENCE_PERIOD}`')

        qr_info = query(
            f'SELECT `id`, `nickname` FROM `{DWTables.INFORMATION}`'
        )

        qr_data_type = query(
            f'SELECT `id`, `datatype` FROM `{DWTables.DATA_TYPE}`')

        '''
        locations = {
            f'{unidecode(name)}': idIBGE
            for name, idIBGE in qr_locations
        }
        '''

        locations = get_location_dict()

        granularities = {f'{unidecode(g)}': i for i, g in qr_granularity}

        rf_periods = {
            (in_date.__str__(), until_date.__str__()): id_rfp
            for id_rfp, in_date, until_date in qr_rf_periods
        }

        info = {
            nickname: idf
            for idf, nickname in qr_info
        }

        dt_type = {
            datatype: iddtp
            for iddtp, datatype in qr_data_type
        }

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

        def join(list_): return ', '.join(list_)

        id_list = [
            f'{row[field]}'
            for field in fields_list
        ]

        q = f"INSERT INTO {DWTables.DATA}"
        q += f"({join(fields_list)})"
        q += f" VALUES ({join(id_list)})"
        print(q)

    def fill_all_data_dw_fields(self, locations, granularities, rf_periods, info, dt_type):
        mapper = Mapper(locations, granularities, rf_periods, info, dt_type)

        actions = {
            DataDWFields.LOCATION: lambda period: mapper.city_name_to_id(period.city_uf),
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
        # self._data_dw_df.apply(self.create_insert_query)

        for _, row in df.iterrows():
            self.create_insert_query(row)
