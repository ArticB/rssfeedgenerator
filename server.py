import os
from flask import Flask, request, send_from_directory
from datetime import datetime
from flask_jsonpify import jsonify
from flask_restful import Resource, Api
import xml.etree.ElementTree as ET 

RSS_FOLDER = './rss'

app = Flask(__name__)

app.config['RSS_FOLDER'] = RSS_FOLDER
api = Api(app)

def parsehtml(content):
    html = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1.0"/><meta http-equiv="X-UA-Compatible" content="ie=edge"/><title>RSS</title></head><body>'+content+'</body></html>'
    return html

@app.route("/rssinput", methods=['POST'])
def rssinput():
    link = request.form['text']
    tree = ET.parse(RSS_FOLDER+'/rss.xml')
    root = tree.getroot()

    return send_from_directory(app.config['RSS_FOLDER'],'rss.xml')


@app.route("/input")
def input():
    return '<form action="/rssinput" method="post" ><input type="text" name="text"/><input type="submit">Submit</input></form>'

@app.route("/")
def hello():
    return jsonify({'text':'Welcome'})

if __name__ == '__main__':
    app.run(host= 'localhost', port=5005)