import json
import random
import string

# import flask modules
# Request - gets details for the request
# Flask - creates the flask app
from flask import Flask, request

# import flask_cors modules
# CORS - enable Cross Origin Resource Sharing
from flask_cors import CORS

# Connect to MongoDB
from credentials import mongodb_parameters
params = mongodb_parameters()
from pymongo import MongoClient

# Setup client and database
client = MongoClient(params['dblink'])
db = client[params['database_name']]

# Create the app and enable CORS
app = Flask(__name__)
CORS(app)

# http://localhost:5000/register
@app.route('/register')
def register():

    reg = {
        'name': request.args.get('name'),
        'uname': request.args.get('email'),
        'password': request.args.get('pass'),
	'uid': ''.join(random.choices(string.ascii_uppercase + string.digits, k=13))
    }
    print(reg)

    db.login.insert_one(reg)
    return 'Good'

# http://localhost:5000/login
@app.route('/login')
def login():

    uname = request.args.get('email')
    password = request.args.get('pass')
    print(uname, password)
    val = db.login.find_one({'uname': uname})
    print(val)
    
    if val == None:
        return 'Bad'
    
    if val['password'] == password:
        return val['name']
    return 'Bad'

# http://localhost:5000/uid
@app.route('/uid')
def udi():

    uname = request.args.get('email')
    val = db.login.find_one({'uname': uname})
    return val['uid']

if __name__ == '__main__':
    app.run()
