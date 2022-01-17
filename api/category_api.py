from resources.authenticate import authenticate
from flask import Flask, request
from postgres_db.category_db import *

class category_api:
    app = Flask(__name__)
    db = category_db()
    auth = authenticate()

    @app.route('/categories', methods = ['GET'])
    def getCategories():
        
        userId = request.args.get('userId')
        return db.getCategories(userId)

    @app.route('/category', methods = ['PUT'])
    def putCategory():
        userId = request.args.get('userId')
        name = request.args.get('name')
        color = request.args.get('color')
        return db.addCategory()

    @app.route('/category', methods = ['DELETE'])
    def deleteCategory():
        return 'unimplemented'

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=7000, debug=True)