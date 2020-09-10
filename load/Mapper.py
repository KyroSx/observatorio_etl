from models.DataPeriode import DataPeriode
from dataclasses import dataclass
from helpers.decoder import decode


@dataclass
class Mapper:
    locations: dict
    granularities: dict
    reference_periods: dict
    info: dict
    data_type: dict

    NOT_FOUND = 'NOT FOUND'

    def city_name_to_id(self, city_uf: str) -> int:
        return self.locations.get(decode(city_uf), self.NOT_FOUND)

    def period_name_to_id(self, period: str) -> int:
        return self.granularities.get(decode(period), self.NOT_FOUND)

    def reference_period_to_id(self, date: tuple) -> int:
        return self.reference_periods.get(date, self.NOT_FOUND)

    def get_information_id(self) -> int:
        return self.info.get('FUNDEB', self.NOT_FOUND)

    def get_data_type_id(self) -> int:
        return self.data_type.get('float', self.NOT_FOUND)
