import json

# import flask modules
# Request - gets details for the request
# Flask - creates the flask app
from flask import Flask, request, send_from_directory, render_template
from jinja2 import TemplateNotFound
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
@app.route('/', defaults={'page': 'index'})
@app.route('/templates/<page>')
def html_lookup(page):
    try:
        return render_template('{}.html'.format(page))
    except TemplateNotFound:
        abort(404)
#@app.route('/')
#def index():
#   return render_template('index.html')
@app.route('/welcome')
def index_welcome():
   return render_template('welcome.html')
@app.route('/python')
def index_Python():
   return render_template('python.html')
@app.route('/WebDev')
def index_WebDev():
   return render_template('WebDev.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)
@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)
@app.route('/test')
def test():
   return '<html><body><h1>Hello World</h1></body></html>'
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
@app.route('/login')
def login():
    return render_template('login.html')
    uname = request.args.get('email')
    password = request.args.get('pass')
    print(uname, password)
    val = db.login.find_one({'uname': uname})
    print(val)
    
    if val == None:
        return 'Bad'
    
    if val['password'] == password:
        return val['name']
#        return render_template('welcome.html')
    return render_template('welcome.html')
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

# http://localhost:5000/uid
@app.route('/uid')
def udi():

    uname = request.args.get('email')
    val = db.login.find_one({'uname': uname})
    return val['uid']
if __name__ == '__main__':
    app.run()
