import pandas
import numpy as np

def get_dataframe():
    file_path = './data/FUNDEB_Municipio.csv'
    columns = ['COD_MUN', 'Município', 'Mês', '2007', '2008']
    encode = 'windows-1252'#'ISO-8859-1'

    fundeb = pandas.read_csv(
        filepath_or_buffer=file_path,
        usecols=columns,
        encoding=encode,
        sep=';',
        decimal=',',
        engine='c',
        nrows=10
    )
    
    return fundeb
