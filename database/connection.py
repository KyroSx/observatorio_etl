import mysql.connector

from . import database_env as db
from mysql.connector import errorcode


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

    def get_city_id_by_name(self, city_name):
        self.start_connection()

        cursor = self.cnx.cursor()
        query = f'SELECT idIBGE FROM locations '
        query += f'WHERE name = \'{city_name}\''
        query += f'and type = \'Município\''

        cursor.execute(query)
        city_id = [x for x in cursor]

        cursor.close()
        self.close_connection()

        return city_id
