import pandas
from dataclasses import dataclass
from .database.Database import Database

from unidecode import unidecode
from .Mapper import Mapper


@dataclass
class Load:
    database: Database
    periode_summed_series: pandas.Series

    _data_dw_df: pandas.DataFrame = pandas.DataFrame([])

    def start(self):
        self.database.start_connection()

        qr_locations = self.database.execute_query(
            'SELECT `name`, `id_ibge` FROM `Location`')

        qr_granularity = self.database.execute_query(
            'SELECT `id`, `granularity` FROM `Granularity`')

        qr_rf_periods = self.database.execute_query(
            'SELECT `id`, `in_date`, `until_date` FROM `ReferencePeriod`')

        qr_info = self.database.execute_query(
            'SELECT `id`, `nickname` FROM `Information`'
        )

        qr_data_type = self.database.execute_query(
            'SELECT `id`, `datatype` FROM `DataType`')

        locations = {
            f'{unidecode(name)}': idIBGE
            for name, idIBGE in qr_locations
        }

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

        mapper = Mapper(locations, granularities, rf_periods, info, dt_type)

        self._data_dw_df['locations_id'] = self.periode_summed_series.apply(
            lambda period: mapper.city_name_to_id(period.city_name))

        self._data_dw_df['granularity_id'] = self.periode_summed_series.apply(
            lambda period: mapper.period_name_to_id(period.periode))

        self._data_dw_df['reference_period_id'] = self.periode_summed_series.apply(
            lambda period: mapper.reference_period_to_id(
                period.reference_periode))

        self._data_dw_df['information_id'] = self.periode_summed_series.apply(
            lambda period: mapper.get_information_id())

        self._data_dw_df['data_type_id'] = self.periode_summed_series.apply(
            lambda period: mapper.get_information_id())

        self._data_dw_df['data'] = self.periode_summed_series.apply(
            lambda period: period.value)

        print(self._data_dw_df)

    def end(self):
        self.database.close_connection()
