from dataclasses import dataclass
from load.repositories.Repository import Repository
from helpers.decoder import decode
from helpers.join import join
from models.DataDW import DWTables


@dataclass
class InformationsRepository:
    repository:  Repository

    __FIELDS_LIST = ['id', 'nickname']
    __TABLE_NAME = DWTables.INFORMATION

    def fetch_informations(self) -> dict:
        cursor_result = self.repository.fetch(
            table=self.__TABLE_NAME,
            field_list=self.__FIELDS_LIST
        )

        return self.__serialize(cursor_result)

    def __serialize(self, cursor) -> dict:
        informations = {
            nickname: idf
            for idf, nickname in cursor
        }

        return informations
