from flask import Flask, request
from user_db import *

app = Flask(__name__)
db = user_db()
authorizations = []

@app.route('/login', methods = ['GET'])
def login():
    email = request.args.get('userId')
    password = request.args.get('userId')
    
    return 'unimplemented'

@app.route('/logout', methods = ['GET'])
def logout():
    token = request.headers.get('auth-token')
    
    authorizations = [s for s in authorizations if s.token != token]

    return 'success'

@app.route('/authentication', methods = ['GET'])
def authentication():
    token = request.headers.get('auth-token')
    user_id = request.args.get('user_id')
    return any(s.user_id == user_id and s.token == token for s in authorizations)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000, debug=True)