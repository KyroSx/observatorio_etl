import database.database_env as db
import mysql.connector
from mysql.connector import errorcode


config = {
  'user': db.DB_USER,
  'password': db.DB_PASSWORD,
  'host': '127.0.0.1',
  'database': db.DB_NAME,
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
