import mysql.connector

from . import database_env as db
from mysql.connector import errorcode


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

    def search_city_name_query(self, city_name):
        if self.cnx is not None:
            cursor = self.cnx.cursor()
            query = f'SELECT idIBGE FROM locations '
            query += f'WHERE name = \'{city_name}\''

            cursor.execute(query)
            city_id = [str(x) for x in cursor]
            print(city_id[0])
