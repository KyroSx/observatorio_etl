import pandas
import numpy as np

def get_dataframe():
    file = '~/TCC/bkBases/FUNDEB-por-Municipio_3.csv'
    encode = "windows-1252"#"ISO-8859-1"
    separator = ';'
    columns = ['COD_MUN', 'Município', 'Mês', '2007', '2008']
    fundeb = pandas.read_csv(filepath_or_buffer=file,
                             encoding=encode,
                             engine="c",
                             sep=separator,
                             decimal=',',
                             nrows=10,
                             usecols=columns)
    return fundeb
