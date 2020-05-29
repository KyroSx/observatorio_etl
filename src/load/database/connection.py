import mysql.connector

from config import database_env as db
from mysql.connector import errorcode
from src.transform.helpers.str_helper import (
    remove_parenthesis, remove_char_from_string)


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
