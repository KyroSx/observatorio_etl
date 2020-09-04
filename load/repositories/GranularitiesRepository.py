from dataclasses import dataclass
from load.repositories.Repository import Repository
from helpers.decoder import decode
from helpers.join import join
from models.DataDW import DWTables


@dataclass
class GranularitiesRepository:
    repository:  Repository

    __FIELDS_LIST = ['id', 'granularity']
    __TABLE_NAME = DWTables.GRANULARITY

    def fetch_granularities(self) -> dict:
        cursor_result = self.repository.fetch(
            table=self.__TABLE_NAME,
            field_list=self.__FIELDS_LIST
        )

        return self.__serialize(cursor_result)

    def __serialize(self, cursor) -> dict:
        granularities = {decode(granularity): _id
                         for _id, granularity in cursor}

        return granularities
