from dataclasses import dataclass
import pandas


@dataclass
class Extract:

    number_of_rows: int = 66829

    csv: str = 'extract/fundeb.csv'
    dataframe: pandas.DataFrame = pandas.DataFrame([])

    def start(self):
        """ Get the dataframe from a csv file  """
        print(f"Extract the {self.csv}")
        self.dataframe = self._get_dataframe()

    def end(self) -> pandas.DataFrame:
        """ Return a dataframe """
        print(f'Returning({__name__}): \n {self.dataframe} \n')
        return self.dataframe

    def _usecols(self):
        cols = [i for i in range(1, 18)]
        del cols[2]
        return cols

    def _get_dataframe(self) -> pandas.DataFrame:
        """ Config for read a csv """
        file_path = self.csv
        encode = "windows-1252"
        cols = self._usecols()

        fundeb = pandas.read_csv(
            filepath_or_buffer=file_path,
            encoding=encode,
            sep=";",
            decimal=",",
            engine="c",
            usecols=cols,
            nrows=self.number_of_rows,
        )

        return fundeb
