from flask import Flask, request
from postgres_db.user_db import user_db
from ..postgres_db.activity_db import *

class authenticate_api:
    app = Flask(__name__)
    db = user_db()
    authorizations = []
    

    @app.route('/login', methods = ['GET'])
    def getActivities():
        email = request.args.get('userId')
        password = request.args.get('userId')
        return 'unimplemented'

    @app.route('/logout', methods = ['GET'])
    def putActivity():
        token = request.headers.get('auth-token')
        
        return 'unimplemented'

    @app.route('/authentication', methods = ['GET'])
    def deleteActivity():
        token = request.headers.get('auth-token')
        return 'unimplemented'

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=7000, debug=True)