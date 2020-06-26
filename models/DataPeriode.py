import pandas
from dataclasses import dataclass
from typing import List


@dataclass
class DataPeriode:
    city_name: str
    uf: str
    index: int
    periode: str
    year: str
    value: float
    reference_periode: tuple = ('', '')

    def get_all_values_tuple(self) -> tuple:
        return (self.city_name, self.uf, self.index,
                self.periode, self.year, self.value,
                self.reference_periode)

    def __str__(self):
        tupled = self.get_all_values_tuple()
        return str(tupled)


def create_data_object(data_dict: dict) -> DataPeriode:
    city_name, uf, year, index, periode, value = data_dict.values()
    data_o = DataPeriode(periode=periode, value=value,
                         year=year, city_name=city_name,
                         uf=uf, index=index)
    return data_o


def create_object_list_from_dict(dict_list: dict) -> List[DataPeriode]:
    data_object_list = []
    for data_dict in dict_list:
        data = create_data_object(data_dict)
        data_object_list.append(data)

    return data_object_list
