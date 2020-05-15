import mysql.connector
import database_env as db

from mysql.connector import errorcode


config = {
    'user': db.DB_USER,
    'password': db.DB_PASSWORD,
    'host': db.HOST,
    'database': db.DB_NAME,
    'raise_on_warnings': True
}


def connect_to_db():
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Something is wrong with your user or password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Database does not exist')
        else:
            print(err)
        cnx.close()
    else:
        return cnx
