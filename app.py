import json

# import flask modules
# Request - gets details for the request
# Flask - creates the flask app
from flask import Flask, request, send_from_directory

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
collection = db[params['collection_name']]

# Create the app and enable CORS
app = Flask(__name__, static_url_path='')
CORS(app)

# Route at which the request is processed
# http://localhost:5000/products
#@app.route('/')
#def root():
#    return app.send_static_file('index.html')
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)
@app.route('/index/')
def root():
    return app.send_static_file('index.html')

@app.route('/products')
def products():

    cursor = collection.find({})
    response = []
    for doc in cursor:
        doc.pop('_id', 0)
        response.append(doc)
    
    # Return json response
    response = json.dumps(response)
    return response

if __name__ == '__main__':
    app.run()
