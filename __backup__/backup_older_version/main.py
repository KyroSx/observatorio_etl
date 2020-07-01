import pandas
import numpy as np
from dataclasses import dataclass, field

from src.extract.dataframe import create_data_frame

from src.load.reference_period import get_reference_period
from src.load.load import apply_locations, get_all_reference_periodes_from_series

from src.transform.standardize import standardize_years_values, fix_city_names

from src.transform.dict_data_object_creation import (
    create_data_object_dict_list,
    calculate_all_periods_sums)

from src.transform.models.Data_Object import (
    create_data_object, create_object_list)


@dataclass
class Main:

    fundeb: pandas.DataFrame = pandas.DataFrame([])
    data_period_object_list = []
    municipio = "Município"

    def extract(self):
        self.fundeb = create_data_frame(1000)

    def show(self):
        for data_period_object in self.data_period_object_list:
            print(data_period_object)

    def transform(self):

        years = [f"{i}" for i in range(2007, 2020)]
        list_data_dicts = []

        for year in years:
            self.fundeb[year] = self.fundeb[year].apply(
                standardize_years_values)

        self.fundeb[self.municipio] = self.fundeb[self.municipio].apply(
            fix_city_names)

        citys = self.fundeb.groupby([self.municipio])
        for city_name, _ in citys:
            ac = citys.get_group(city_name)
            a = str(ac.iloc[0]['UF'])
            list_data_dicts += calculate_all_periods_sums(ac, city_name, a)

        self.data_period_object_list = create_object_list(list_data_dicts)

        df_o = pandas.DataFrame(
            self.data_period_object_list, columns=['Object'])

        df_o['Object'] = get_all_reference_periodes_from_series(df_o['Object'])
        apply_locations(df_o['Object'])

    def load(self):
        ''  # load(self.data_period_object_list)


if __name__ == "__main__":
    main = Main()
    main.extract()
    main.transform()
    # main.load()
