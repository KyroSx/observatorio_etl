
import os
import mysql.connector
from mysql.connector import errorcode

from dotenv import load_dotenv
load_dotenv()


class Database:
    cnx = ''
    config = {
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('HOST'),
        'database': os.getenv('DB_NAME'),
        'raise_on_warnings': True
    }

    def start_connection(self):
        print(self.config)
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
