from token_generator import generate_unique_token
from flask import Flask, request
from authentication_db import *
from authenticated import *
authorizations = []


def removeValue(authorizations, token):
    authorizations = filter(lambda x: x['token'] !=token, authorizations)
    return authorizations

app = Flask(__name__)
db = authentication_db()

@app.route('/login', methods = ['GET'])
def login():
    email = request.args.get('email')
    password = request.args.get('password')
    
    id = db.verifyUser(email, password)
    
    if(id == None): return {'success' : False}

    token = generate_unique_token(authorizations)

    authorizations.append({'token' : token, 'user_id' : id})

    return {'success':True , 'token' : token , 'user_id': id}

@app.route('/logout', methods = ['GET'])
def logout():
    token = request.args.get('token')

    authentication = next(x for x in authorizations if x['token'] == token)

    authorizations.remove(authentication)
  

    return {'success' : not any(s['token'] == token for s in authorizations)}

@app.route('/authentication', methods = ['GET'])
def authentication():
    token = request.args.get('token')
    user_id = int(request.args.get('user_id'))
    return {
        'authenticated': any(x['user_id'] == user_id and x['token'] == token for x in authorizations), 
        'user_id':authorizations[0]['user_id'] , 
        'given_user_id':user_id, 
        'token':authorizations[0]['token'],
        'given_token':token
        }

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
    
