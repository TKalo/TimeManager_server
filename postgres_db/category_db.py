import imp
import json

from resources.postgres_functions import sql_to_json
from ..idb.category_idb import category_idb
from psycopg2 import Error

from connection import connect

class category_db(category_idb):

    connection = connect()

    def getCategories(self, userId):
        cursor = self.connection.cursor()
        
        cursor.execute('SELECT * FROM category WHERE userId == {userId};'.format(userId))
        
        results = cursor.fetchall()
        
        row_headers=[x[0] for x in cursor.description]
        
        return sql_to_json(results, row_headers)

    def addCategory(self, userId, name, color):
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO category (userId, name, color) VALUES (\'{userId}\',\'{name}\',\'{color}\')'.format(userId,name,color))
        try:
            cursor.commit()
        except Error as e:
            return e
        return 'success'

    def deleteCategories(userId, name):
        pass