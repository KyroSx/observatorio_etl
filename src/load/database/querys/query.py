from dataclasses import dataclass
from src.load.database.connection import Database, create_database_object
from src.transform.helpers.str_helper import (
    remove_parenthesis, remove_char_from_string)


def create_query_object(database: Database):
    return Querys(database)


@dataclass
class Querys:
    database: Database

    def format_query_result_as_str_list(self, cursor) -> list:
        results = [str(result) for result in cursor]

        results = map(lambda cid: remove_parenthesis(cid),
                      results)

        results = map(lambda cid: remove_char_from_string(cid, ','),
                      results)

        return list(results)

    def get_query_results_formated(self, query: str):
        self.database.start_connection()
        cursor = self.database.cnx.cursor(buffered=True)

        cursor.execute(query)

        result = self.format_query_result_as_str_list(cursor)

        cursor.close()
        self.database.close_connection()

        return result

    def get_str_fields_generic(self, data: dict) -> list:

        fields, table, where = data.values()

        formated_fields = ', '.join(fields)

        query = f"SELECT {formated_fields} FROM {table}"

        if where:
            query += f" WHERE {where}"

        result = self.get_query_results_formated(query)
        return result

    # dont have values in database
    def get_reference_period_id_from_periods_dates(self, info: dict):
        in_date, until_date = info.values()

        data = {
            "fields": ['*'],
            "table": 'ReferencePeriode',
            "where": f'`in`=\'{in_date}\' and until=\'{until_date}\''
        }

        ref_per = self.get_str_fields_generic(data)
        return ref_per

    def get_city_id_by_name(self, city_name):

        data = {
            "fields": ["idIBGE"],
            "table": "locations",
            "where": f'name=\'{city_name}\' and type=\'Municipio\''
        }

        city_id = self.get_str_fields_generic(data)

        return city_id
