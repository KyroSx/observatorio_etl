import pandas

def get_dataframe():
    file = '~/TCC/bkBases/FUNDEB-por-Municipio_3.csv'
    encode = "ISO-8859-1"
    separator = ';'
    columns = [i for i in range(6)]
    #columns = ['COD_MUN', 'Município', 'Mês', '2007', '2019']
    fundeb = pandas.read_csv(filepath_or_buffer=file,
                             encoding=encode,
                             engine="python",
                             sep=separator,
                             usecols=columns)
    return fundeb
