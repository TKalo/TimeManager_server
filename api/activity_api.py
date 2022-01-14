from flask import Flask, request
from ..postgres_db.activity_db import *

class api:
    app = Flask(__name__)
    db = activity_db()

    @app.route('/activities', methods = ['GET'])
    def getActivities():
        return 'unimplemented'

    @app.route('/activity', methods = ['PUT'])
    def putActivity():
        return 'unimplemented'

    @app.route('/activity', methods = ['DELETE'])
    def deleteActivity():
        return 'unimplemented'

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=7000, debug=True)