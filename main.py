import pandas

from src.load.database.connection import Database
from src.transform.standardize import standardize
from src.transform.period import get_period_object_list

from src.transform.models.Data_Object import create_data_object
from src.extract.dataframe import create_data_frame


fundeb = create_data_frame(number_of_rows=12)

years = [f"{i}" for i in range(2007, 2020)]
space = "-" * 33
list_data_objects = []


for year in years:
    fundeb[year] = fundeb[year].apply(standardize)

citys = fundeb.groupby("Município")
for city_name, city_df in citys:

    print(f'Loading for {city_name}...')
    period_type = "yearly".lower()

    for year in years:
        list_data_objects += get_period_object_list(
            period_type, city_df, city_name, year)

[print(f'{x}\n{space}')
 for x in list_data_objects[::-1]]
