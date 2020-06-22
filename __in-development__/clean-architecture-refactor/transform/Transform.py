import pandas
from dataclasses import dataclass
from typing import Tuple, List, Callable

from models.Fundeb import Fundeb
from models.DataPeriode import create_object_list_from_dict


@dataclass
class Transform:
    fundeb_obj_validated: Fundeb
    periode_summed_series: pandas.Series = pandas.Series([])

    def start(self):
        print(f'Transforming: \n {self.fundeb_obj_validated}')

        dataframe_grouped_by_city = self.fundeb_obj_validated \
            .get_dataframe_grouped_by_city()

        list_data_dicts = []
        for name, df in dataframe_grouped_by_city.__iter__():
            uf = str(df.iloc[0]['UF'])
            list_data_dicts += self._calculate_all_periods_sums(
                df, name, uf)

        data_period_object_list = create_object_list_from_dict(
            list_data_dicts)

        self.periode_summed_series = pandas.Series(data_period_object_list)

    def end(self):
        return self.periode_summed_series

    def _calculate_all_periods_sums(self, city_grouped, city_name: str,
                                    city_uf: str):
        periods = ['bimonthly', 'quarterly',
                   'half-yearly', 'yearly']
        list_of_periodes_sum = []
        list_data_dicts = []
        for period in periods:
            list_of_periodes_sum = self._calculate_period(period, city_grouped)
            list_data_dicts += self._create_data_object_dict_list(
                city_name, city_uf, list_of_periodes_sum)

        return list_data_dicts

    def _create_data_object_dict_list(self, city_name: str,
                                      city_uf: str,
                                      list_of_periodes_sum: list):
        list_data_dicts = []
        for list_periode in list_of_periodes_sum:
            for periode_sum in list_periode:
                year, index, periode, value = periode_sum

                data_dict = {
                    'city_name': city_name,
                    'UF': city_uf,
                    'year': year,
                    'index': index,
                    'periode': periode,
                    'value': value
                }

                list_data_dicts.append(data_dict)
        return list_data_dicts

    def _calculate_period(self, period: str,
                          city_grouped: pandas.DataFrame) -> List[int]:

        inverval, start_inteval, end_interval = \
            self._period_options(period)

        years = [f"{year}" for year in range(2007, 2020)]

        result_list = []
        for index in inverval:
            sliced = city_grouped[
                (city_grouped['Mês'] >= (start_inteval(index))) &
                (city_grouped['Mês'] <= (end_interval(index)))
            ].sum()

            result_years_list = []
            for year in years:
                value = round(sliced[year], 2)
                result = (year, index, period, value)
                result_years_list.append(result)

            result_list.append(result_years_list)

        return result_list

    def _period_constants(self, period: str) -> int:
        periodes = {
            "bimonthly": 2,
            "quarterly": 3,
            "half-yearly": 6,
            "yearly": 12
        }
        period_value = periodes.get(period, "Not a valid period")

        return period_value

    def _period_options(self, period: str) -> Tuple[
            List[int], Callable[[int], int], Callable[[int], int]]:

        period_value = self._period_constants(period)
        total_months = 12
        final_interval = (total_months / period_value) + (1)

        inverval = range(1, int(final_interval))
        def start_interval(i): return (i*period_value)-(period_value-1)
        def end_interval(i): return (i*period_value)

        return (inverval, start_interval, end_interval)
