from dataclasses import dataclass
from load.repositories.Repository import Repository
from helpers.decoder import decode
from helpers.join import join
from models.DataDW import DWTables


@dataclass
class DataTypesRepository:
    repository:  Repository

    __FIELDS_LIST = ['id', 'datatype']
    __TABLE_NAME = DWTables.DATA_TYPE

    def fetch_data_types(self) -> dict:
        cursor_result = self.repository.fetch(
            table=self.__TABLE_NAME,
            field_list=self.__FIELDS_LIST
        )

        return self.__serialize(cursor_result)

    def __serialize(self, cursor) -> dict:
        data_types = {
            datatype: id_dtp
            for id_dtp, datatype in cursor
        }

        return data_types
