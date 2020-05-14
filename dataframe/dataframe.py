import pandas
import numpy as np


def usecols():
    cols = [i for i in range(1, 18)]
    del cols[2]
    return cols


def get_dataframe():
    file_path = "./data/FUNDEB_Municipio.csv"
    encode = "windows-1252"
    cols = usecols()

    fundeb = pandas.read_csv(
        filepath_or_buffer=file_path,
        encoding=encode,
        sep=";",
        decimal=",",
        engine="c",
        usecols=cols,
        nrows=12,
    )

    return fundeb
