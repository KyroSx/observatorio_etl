import pandas
from dataclasses import dataclass
from models.DataPeriode import DataPeriode
from typing import Tuple, List, Callable


@dataclass
class ReferencePeriode:

    def get_reference_period(self, period_type, year, index) -> tuple:
        start_day = 1

        start_month_list, ratio = self._referece_period_strateggy(period_type)

        end_day, start_month, end_month = self._get_day_and_month(
            start_month_list, index, ratio)

        is_leap = self._is_leap_year(year)
        if is_leap and end_month == 2:
            end_day += 1

        in_date = f'{year}-{start_month}-{start_day}'
        until_date = f'{year}-{end_month}-{end_day}'

        return in_date, until_date

    def _referece_period_strateggy(self, period_type: str) -> tuple:
        """ Design pattern to return calculations variables """
        periods = {
            'bimonthly': ([x for x in range(1, 12) if x % 2 == 1], 2),
            'quarterly': ([x for x in range(1, 12, 3)], 3),
            'half-yearly': ([x for x in range(1, 12, 6)], 6),
            'yearly': ([x for x in range(1, 12, 12)], 12)
        }
        return periods.get(period_type)

    def _get_day_and_month(self, start_month_list: list, index: int, ratio: int):
        """ Return day and month variables to calculate period """
        delta = index*ratio
        end_day = self._get_end_day(delta)
        start_month = start_month_list[index-1]
        end_month = delta

        return end_day, start_month, end_month

    def _get_end_day(self, month: int) -> int:
        ''' Return the last day of a month '''
        return {
            2: 28,
            3: 31,
            4: 30,
            6: 30,
            8: 31,
            9: 30,
            10: 31,
            12: 31
        }.get(month)

    def _is_leap_year(self, year: str) -> bool:
        """ Identify if a year is leap """
        year = int(year)

        if year % 4 == 0:
            if year % 100 != 0:
                return True
        if year % 400 == 0:
            return True

        return False
