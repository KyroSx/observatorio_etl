from dataclasses import dataclass
from typing import List
from load.database.Database import Database
from helpers.join import join


@dataclass
class Repository:
    database: Database

    def fetch(self, table: str, field_list: list) -> dict:
        self.__table = table
        self.__field_list = field_list

        query = self.__get_query()

        return self.database.execute_query(query)

    @property
    def __query_params(self) -> str:
        formated = [f'`{field}`'
                    for field in self.__field_list]

        return join(formated)

    def __get_query(self) -> str:
        query = f'SELECT {self.__query_params}'
        query += f'FROM `{self.__table}`'

        return query
