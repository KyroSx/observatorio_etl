import mysql.connector
from mysql.connector import errorcode

from database_env import *

config = {
  'user': DB_USER,
  'password': DB_PASSWORD,
  'host': '127.0.0.1',
  'database': DB_NAME,
  'raise_on_warnings': True
}

def connect_to_db():
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()
    else:
        return cnx            
