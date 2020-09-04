import pandas
from models.DataPeriode import DataPeriode


class ReferencePeriode:
    in_date: str
    until_date: str

    def start(self, period_type: str, year: str, index: int):
        in_date, until_date = self.get_reference_period(
            period_type, year, index)

        self.in_date = in_date
        self.until_date = until_date

    def end(self) -> tuple:
        return (self.in_date, self.until_date)

    def format_date(self, year, month, day) -> str:
        return f'{year}-{month}-{day}'

    def get_reference_period(self, period_type: str, year: str, index: int) -> tuple:
        start_day = '01'

        start_month_list, ratio = self.reference_period_strategy(period_type)

        end_day, start_month, end_month = self.get_day_and_month(
            start_month_list, index, ratio)

        if end_month == 2:
            if self.is_leap_year(year):
                end_day += 1

        in_date = self.format_date(year, start_month, start_day)
        until_date = self.format_date(year, end_month, end_day)

        return in_date, until_date

    def reference_period_strategy(self, period_type: str) -> tuple:
        def odd_list(): return [x for x in range(1, 12) if x % 2 == 1]

        def list_from_steps(step): return [x for x in range(1, 12, step)]

        periods = {
            'bimonthly': (odd_list(), 2),
            'quarterly': (list_from_steps(3), 3),
            'half-yearly': (list_from_steps(6), 6),
            'yearly': (list_from_steps(12), 12)
        }

        return periods.get(period_type)

    def format_month(self, month: int) -> str or int:
        return f'0{month}' if month < 10 else month

    def get_day_and_month(self, start_month_list: list, index: int, ratio: int) -> tuple:
        delta = index*ratio
        end_day = self.get_end_day(delta)
        start_month = start_month_list[index-1]
        end_month = delta

        end_month = self.format_month(end_month)
        start_month = self.format_month(start_month)

        return end_day, start_month, end_month

    def get_end_day(self, month: int) -> int:
        last_day_of_month = {
            2: 28,
            3: 31,
            4: 30,
            6: 30,
            8: 31,
            9: 30,
            10: 31,
            12: 31
        }

        return last_day_of_month.get(month)

    def is_leap_year(self, year: str) -> bool:
        def is_multiple_of(number) -> bool: return int(year) % number == 0

        return is_multiple_of(4) and not is_multiple_of(100) or is_multiple_of(400)
