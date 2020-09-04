from dataclasses import dataclass
import pandas


@dataclass
class Fundeb:
    dataframe: pandas.DataFrame
    years = [f'{y}' for y in range(2007, 2020)]

    uf: str = 'UF'
    city: str = 'Município'

    def __str__(self):
        return self.dataframe

    def get_all_city_series(self) -> pandas.Series:
        return self.dataframe[self.city]

    def get_all_city_uf_series(self) -> pandas.Series:
        return self.dataframe[self.city].copy(deep=False)\
            + '-'\
            + self.dataframe[self.uf].copy(deep=False)

    def get_year_series(self, year: str) -> pandas.Series:
        if year in year:
            return self.dataframe[year]

    def get_dataframe_grouped_by_city(self) -> pandas.DataFrame:
        return self.dataframe.groupby([self.city, self.uf])
