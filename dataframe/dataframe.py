import pandas
import numpy as np

def get_dataframe():
    file_path = './data/FUNDEB_Municipio.csv'
    encode = 'windows-1252'#'ISO-8859-1'
    cols = [i for i in range(1,18)]
    del cols[2]
    
    fundeb = pandas.read_csv(
        filepath_or_buffer=file_path,
        encoding=encode,
        sep=';',
        decimal=',',
        engine='c',
        usecols=cols,
        nrows=12
    )
    
    return fundeb
