import mysql.connector

from . import database_env as db
from mysql.connector import errorcode
from helpers.str_helper import remove_parenthesis, remove_char_from_string


def create_database_object():
    return Database()


class Database:
    cnx = ''
    config = {
        'user': db.DB_USER,
        'password': db.DB_PASSWORD,
        'host': db.HOST,
        'database': db.DB_NAME,
        'raise_on_warnings': True
    }

    def start_connection(self):
        try:
            self.cnx = mysql.connector.connect(**self.config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Something is wrong with your user or password')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('Database does not exist')
            else:
                print(err)

    def close_connection(self):
        self.cnx.close()

    def format_query_result_as_str_list(self, cursor) -> list:
        results = [str(result) for result in cursor]

        results = map(lambda cid: remove_parenthesis(cid),
                      results)

        results = map(lambda cid: remove_char_from_string(cid, ','),
                      results)

        return list(results)

    def get_query_results_formated(self, query: str):
        self.start_connection()
        cursor = self.cnx.cursor(buffered=True)

        cursor.execute(query)

        result = self.format_query_result_as_str_list(cursor)

        cursor.close()
        self.close_connection()

        return result

    def get_str_fields_generic(self, data) -> list:

        fields, table, where = data.values()

        formated_fields = ', '.join(fields)

        query = f"SELECT {formated_fields} FROM {table}"

        if where:
            query += f" WHERE {where}"

        result = self.get_query_results_formated(query)
        return result

    def get_reference_period_id_from_periods_dates(self, info):
        in_date, until_date = info.values()

        data = {
            "fields": ['*'],
            "table": 'ReferencePeriode',
            "where": f'`in`=\'{in_date}\' and until=\'{until_date}\''
        }

        ref_per = self.get_str_fields_generic(data)

    def get_city_id_by_name(self, city_name):

        data = {
            "fields": ["idIBGE"],
            "table": "locations",
            "where": f'name=\'{city_name}\' and type=\'Municipio\''
        }

        city_id = self.get_str_fields_generic(data)

        return city_id
