import pandas

from database.connection import connect_to_db
from dataframe.dataframe import get_dataframe
from dataframe.standardize import standardize
from periods.period import get_period

fundeb = get_dataframe()

years = [f'{i}' for i in range(2007, 2020)]
months = [i+1 for i in range(12)]
space = '-' * 33

for year in years:
    fundeb[year] = fundeb[year].apply(standardize)

year = '2019'
print(get_period(
    "bimestral",
    fundeb,
    year
))
