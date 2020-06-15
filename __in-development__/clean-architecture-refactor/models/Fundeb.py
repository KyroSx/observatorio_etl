from dataclasses import dataclass
import pandas


@dataclass
class Fundeb:
    dataframe: pandas.DataFrame
    years = [f'{y}' for y in range(2007, 2020)]

    uf: str = 'UF'
    city: str = 'Município'

    def __str__(self):
        fundeb_str = f" {self.city} | {self.uf} | {self.years}"
        return fundeb_str

    def get_all_city_series(self) -> pandas.Series:
        """ Returns a Fundeb Series with all cities """
        return self.dataframe[self.city]

    def get_year_series(self, year: str) -> pandas.Series:
        """ Returns Fundeb Series in the year provided """
        if year in year:
            return self.dataframe[year]

    def get_dataframe_grouped_by_city(self) -> pandas.DataFrame:
        return self.dataframe.groupby(self.city)
