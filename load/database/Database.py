import os
import mysql.connector
from mysql.connector import errorcode, cursor

from dotenv import load_dotenv
load_dotenv()


class Database:
    connection = ''
    config = {
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('HOST'),
        'database': os.getenv('DB_NAME'),
        'raise_on_warnings': True
    }

    def start_connection(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            print('🎲 connection started on the db:', self.config['database'])
        except mysql.connector.Error as err:
            print('🚫 db connection error')
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise ValueError(
                    'Something is wrong with your user or password')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise ValueError('Database does not exist')
            else:
                raise ValueError(err)

    def close_connection(self):
        try:
            self.connection.close()
            print('🔌 Connection closed')
        except:
            print('Failed to close connection')

    def execute_query(self, query: str) -> list:
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)

            result = [c for c in cursor]

            return result
        except:
            print('Something went wrong with the query')
        finally:
            cursor.close()
