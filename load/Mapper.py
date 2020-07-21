from unidecode import unidecode
from models.DataPeriode import DataPeriode


def get_id():
    import random

    return random.randint(1, 100)


class Mapper:
    locations: dict = {}
    granularities: dict = {}
    reference_periods: dict = {}
    info: dict = {}
    data_type: dict = {}

    def __init__(self, locations: dict, granularities: dict,
                 reference_periods: dict, info: dict, data_type: dict):
        self.locations = locations
        self.granularities = granularities
        self.reference_periods = reference_periods
        self.info = info
        self.data_type = data_type

    def city_name_to_id(self, city_name: str) -> int:
        unidecoded_city_name = unidecode(city_name)
        location_id = self.locations.get(
            unidecoded_city_name, 'NOT FOUND')

        return location_id

    def period_name_to_id(self, period: str) -> int:
        unidecode_period_name = unidecode(period)
        granularity_id = self.granularities.get(
            unidecode_period_name, 'NOT FOUND')

        return granularity_id

    def reference_period_to_id(self, date: tuple) -> int:
        rf_period_id = self.reference_periods.get(date, 'NOT FOUND')

        return rf_period_id

    def get_information_id(self):
        info_id = self.info.get('FUNDEB', 'NOT FOUND')

        return info_id

    def get_data_type_id(self):
        data_type_id = self.data_type.get('float', 'NOT FOUND')

        return data_type_id
