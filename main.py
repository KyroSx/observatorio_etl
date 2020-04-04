from database.connection import connect_to_db
from dataframe.dataframe import get_dataframe
from dataframe.standardize import standardize
import pandas
import locale

fundeb = get_dataframe()
locale.setlocale(locale.LC_NUMERIC, "en_DK.UTF-8")

'''
fundeb['2007'] = fundeb['2007'] \
    .str.replace(r'[()]', '', regex=True ) \
    #.str.replace(r'', locale.atof(x), regex=True)
'''
a = fundeb['2007']
print(f'Entry: \n{a} \nOut:')
print(fundeb['2007'].apply(standardize))
#columns_2 = parallel(fundeb['2008'])
#fundeb['2008'] = pandas.Series(columns_2)
