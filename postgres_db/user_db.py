from user_idb import user_idb
from postgres_functions import *

from connection import connect

class user_db(user_idb):

    connection = connect()

    def __init__(self):
        pass
    
    def __del__(self):
        self.connection.close()

    def getUser(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM my_user WHERE id = \'{user_id}\';'.format(user_id = user_id))
        return sql_to_json(cursor)

    def addUser(self, email, password):      
        sql = 'INSERT INTO my_user (email, password) VALUES (\'{email}\',\'{password}\')'.format(email=email,password=password)
        
        return commit_or_fail(self.connection, sql)

    def editUser(self, user_id, password):      
        sql = 'UPDATE my_user SET password = \'{password}\' WHERE id=\'{user_id}\';'.format(password=password,user_id=user_id)
        
        return commit_or_fail(self.connection, sql)

    def deleteUser(self, user_id):
        sql = 'DELETE FROM umy_userser WHERE id=\'{user_id}\';'.format(user_id=user_id)
        
        return commit_or_fail(self.connection, sql)
