import pandas


class DataFrame:

    def usecols(self):
        cols = [i for i in range(1, 18)]
        del cols[2]
        return cols

    def get_dataframe(self, number_of_rows):
        file_path = "src/extract/csv/FUNDEB_Municipio.csv"
        encode = "windows-1252"
        cols = self.usecols()

        fundeb = pandas.read_csv(
            filepath_or_buffer=file_path,
            encoding=encode,
            sep=";",
            decimal=",",
            engine="c",
            usecols=cols,
            nrows=number_of_rows,
        )

        return fundeb


def create_data_frame(number_of_rows=66829):
    df_oo = DataFrame()
    if number_of_rows is not None:
        return df_oo.get_dataframe(number_of_rows)
