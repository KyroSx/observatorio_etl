import pandas

from database.connection import connect_to_db
from dataframe.dataframe import get_dataframe
from dataframe.standardize import standardize
from periods.period import get_period

fundeb = get_dataframe()

years = [f"{i}" for i in range(2007, 2020)]
space = "-" * 33

for year in years:
    fundeb[year] = fundeb[year].apply(standardize)

citys = fundeb.groupby("Município")
for city_name, city_df in citys:
    for year in years:
        city_period_sum = get_period("anual", city_df, city_name, year)

        print(f"{city_name}#{year}:")
        print(f"sum is: {city_period_sum}")
        print(space)
