import imp
import json
from queue import Empty
from psycopg2 import Error

from connection import connect

class authentication_db():

    connection = connect()

    def verifyUser(self, email, password):
        cursor = self.connection.cursor()
        cursor.execute('SELECT id FROM my_user WHERE email = \'{email}\' AND password = \'{password}\';'.format(email = email, password = password))
        id = cursor.fetchall()
        if(len(id) != 0):   return id[0][0]
        else:               return None
