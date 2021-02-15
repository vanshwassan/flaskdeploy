from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import loads, dumps
from flask import jsonify, request
import json
import pymongo

app = Flask(__name__)
app.secret_key = "Key123"



@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response



app.config['MONGO_URI'] = "mongodb://localhost:27017/main_db"
mongo = PyMongo(app)

## API ROUTES ##

@app.route('/api/v1/')
def resp():
    resp = "API Version Beta - 1.0"
    status = "DB and Server is working, all chill"
    return jsonify(resp, status)

@app.route('/api/v1/get')
def get_projects():
    project = mongo.db.ico.find()
    resp = dumps(project)
    a = json.loads(resp)
    final = jsonify(a)
    return final

@app.route('/api/v1/get/<ticker>')
def get_project(ticker):
    p = mongo.db.ico.find_one({'ticker': ticker})
    resp = dumps(p)
    a = json.loads(resp)
    final = jsonify(a)
    return final

if __name__ == "__main__":
    app.run(debug=True)
