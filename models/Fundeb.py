from dataclasses import dataclass
import pandas
from .FundebColumns import FundebColumns


@dataclass
class Fundeb:
    dataframe: pandas.DataFrame
    years = FundebColumns.YEARS

    city = FundebColumns.CITY_NAME
    uf = FundebColumns.UF

    def __str__(self):
        return self.dataframe

    def get_all_city_series(self) -> pandas.Series:
        return self.dataframe[FundebColumns.CITY_NAME]

    def get_all_city_uf_series(self) -> pandas.Series:
        return self.dataframe[FundebColumns.CITY_NAME] + '-' + self.dataframe[FundebColumns.UF]

    def get_year_series(self, year: str) -> pandas.Series:
        if year in year:
            return self.dataframe[year]

    def get_dataframe_grouped_by_city(self) -> pandas.DataFrame:
        return self.dataframe.groupby([FundebColumns.CITY_NAME,
                                       FundebColumns.UF])
