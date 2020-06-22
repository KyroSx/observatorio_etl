import pandas
from dataclasses import dataclass
from typing import Tuple, List, Callable

from models.DataPeriode import DataPeriode
from .ReferencePeriode import ReferencePeriode


@dataclass
class Stage:
    periode_summed_series: pandas.Series
    reference_periode: ReferencePeriode = ReferencePeriode()

    def start(self):
        self.periode_summed_series = self.periode_summed_series.apply(
            self.apply_reference_periode)

    def end(self) -> List[DataPeriode]:
        return self.periode_summed_series

    def apply_reference_periode(self, data_periode: DataPeriode) -> DataPeriode:
        data: tuple = data_periode.get_all_values_tuple()

        _city_name, _uf, index, periode, year, _value, reference_periode = data

        reference_periode = self.reference_periode.get_reference_period(
            periode, year, index)

        data_periode.reference_periode = reference_periode

        print(data_periode.reference_periode)

        return data_periode
