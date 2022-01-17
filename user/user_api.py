from flask import Flask, request
from user_db import *

app = Flask(__name__)
db = user_db()

@app.route('/get', methods = ['GET'])
def getUser():
    user_id = request.args.get('userId')

    return db.getUser(user_id)

@app.route('/add', methods = ['GET'])
def addUser():
    email = request.args.get('email')

    password = request.args.get('password')

    return db.addUser(email, password)

@app.route('/edit', methods = ['GET'])
def editPassword():
    user_id = request.args.get('userId')

    password = request.args.get('password')

    return db.editUser(user_id, password)

@app.route('/delete', methods = ['GET'])
def deleteCategory():
    user_id = request.args.get('userId')

    return db.deleteUser(user_id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000, debug=True)