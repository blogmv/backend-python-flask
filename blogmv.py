from flask import Flask, request, escape
from flask.blueprints import Blueprint
from domain.article import Article
from domain.comment import Comment
from json_serializer import JSONEncoder
import json
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)









@app.route("/")
def home():
    return "OK"