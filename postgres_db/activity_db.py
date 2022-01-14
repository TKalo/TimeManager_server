import imp
import json
from ..idb.activity_idb import activity_idb
from psycopg2 import Error

from db_connection import connect

class activity_db(activity_idb):

    connection = connect()

    def getActivities(userId):
        pass

    def addActivity(userId, category, starttime, endtime):
       pass

    def deleteActivity(activityId):
       pass