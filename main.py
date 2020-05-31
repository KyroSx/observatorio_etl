import pandas
import numpy as np
from dataclasses import dataclass, field

from src.load.database.connection import Database
from src.load.database.querys.query import create_query_object
from src.load.reference_period import get_reference_period

from src.transform.standardize import standardize
from src.transform.period import calculate_period

from src.extract.dataframe import create_data_frame
from src.transform.dict_data_object_creation import (
    create_data_object_dict_list,
    calculate_all_periods_sums)

from src.transform.models.Data_Object import (
    create_data_object, create_object_list)


@dataclass
class Main:

    fundeb: pandas.DataFrame = pandas.DataFrame([])
    data_period_object_list = []

    def extract(self):
        self.fundeb = create_data_frame(120)

    def show(self):
        for data_period_object in self.data_period_object_list:
            if data_period_object.location_city_name == 'Acrelândia':
                print(data_period_object)

    def transform(self):

        years = [f"{i}" for i in range(2007, 2020)]
        list_data_dicts = []

        for year in years:
            self.fundeb[year] = self.fundeb[year].apply(standardize)

        citys = self.fundeb.groupby(["Município"])
        for city_name, _ in citys:
            ac = citys.get_group(city_name)
            list_data_dicts += calculate_all_periods_sums(ac, city_name)

        self.data_period_object_list = create_object_list(list_data_dicts)

    def load(self):
        for data_period_object in self.data_period_object_list:
            period, index, year = data_period_object.granularity,\
                data_period_object.index, data_period_object.location_year
            in_d, until_d = get_reference_period(period, year, index)

            d = Database()
            q = create_query_object(d)
            print(q.get_granularity_id_from_period(period))


if __name__ == "__main__":
    main = Main()
    main.extract()
    main.transform()
    main.load()
