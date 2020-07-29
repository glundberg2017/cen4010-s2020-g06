import mysql.connector
from mysql.connector import Error

class DatabaseAdapter:
    def __init__(self, host='', username='', password=''):
        self.host = host
        self.username = username
        self.password = password

    def create_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.username,
                passwd=self.password
            )
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection



##
## TEST - create an instance of DatabaseAdapter and try to connect to it
db_adapter = DatabaseAdapter('lamp.eng.fau.edu', 'cen4010s2020_g06', 'faueng2020')
connection = db_adapter.create_connection()