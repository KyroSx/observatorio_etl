from dataclasses import dataclass
from load.repositories.Repository import Repository
from helpers.decoder import decode
from helpers.join import join
from models.DataDW import DWTables


@dataclass
class ReferencePeriodRepository:
    repository:  Repository

    __FIELDS_LIST = ['id', 'in_date', 'until_date']
    __TABLE_NAME = DWTables.REFERENCE_PERIOD

    def fetch_reference_periods(self) -> dict:
        cursor_result = self.repository.fetch(
            table=self.__TABLE_NAME,
            field_list=self.__FIELDS_LIST
        )

        return self.__serialize(cursor_result)

    def __serialize(self, cursor) -> dict:
        rf_periods = {
            (in_date.__str__(), until_date.__str__()): id_rfp
            for id_rfp, in_date, until_date in cursor
        }

        return rf_periods
