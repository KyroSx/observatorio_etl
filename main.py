import pandas
from Data import Data_Object
# from database.connection import connect_to_db
from dataframe.dataframe import get_dataframe
from dataframe.standardize import standardize
from periods.period import get_period

fundeb = get_dataframe()

years = [f"{i}" for i in range(2007, 2020)]
space = "-" * 33
list_data_objects = []

for year in years:
    fundeb[year] = fundeb[year].apply(standardize)

citys = fundeb.groupby("Município")
for city_name, city_df in citys:
    for year in years:
        period_type = "semestral"
        city_period_sum = get_period(period_type, city_df, city_name, year)
        d = Data_Object(period_type, city_period_sum, year, city_name)
        list_data_objects.append(d)
        print(space)

'''
[print(f'{x}\n{space}')
 for x in list_data_objects]
'''
