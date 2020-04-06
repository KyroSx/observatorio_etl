from database.connection import connect_to_db
from dataframe.dataframe import get_dataframe
from dataframe.standardize import standardize
import pandas
import locale

fundeb = get_dataframe()

a = fundeb['2007']
print(f'Entry: \n{a} \nOut:')
print(fundeb['2007'].apply(standardize))
