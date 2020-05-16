import pandas

from database.connection import Database
from dataframe.dataframe import get_dataframe
from dataframe.standardize import standardize
from periods.period import get_period_object_list

fundeb = get_dataframe()

years = [f"{i}" for i in range(2007, 2020)]
space = "-" * 33
list_data_objects = []

for year in years:
    fundeb[year] = fundeb[year].apply(standardize)

citys = fundeb.groupby("Município")
for city_name, city_df in citys:
    print(f'Loading for {city_name}...')
    for year in years:
        period_type = "anual".lower()
        list_data_objects += get_period_object_list(
            period_type, city_df, city_name, year)

a = []
[a.append(x)
 for x in list_data_objects[::-1] if x.location_city_name == 'Assis Brasil']

db = Database()
db.start_connection()

db.search_city_name_query('Acrêlandia')

db.close_connection()
