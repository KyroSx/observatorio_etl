from dataclasses import dataclass
from load.repositories.Repository import Repository
from helpers.decoder import decode
from helpers.join import join
from models.DataDW import DWTables


@dataclass
class LocationsRepository:
    repository:  Repository

    __FIELDS_LIST = ['name', 'parent_state_nickname', 'id_ibge']
    __TABLE_NAME = DWTables.LOCATION

    def fetch_locations(self) -> dict:
        cursor_result = self.repository.fetch(
            table=self.__TABLE_NAME,
            field_list=self.__FIELDS_LIST
        )

        return self.__serialize(cursor_result)

    def __serialize(self, cursor) -> dict:
        locations = {
            decode(f'{name}-{state}'): idIBGE
            for name, state, idIBGE in cursor
        }

        return locations
