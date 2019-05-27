import os
import rssgenerator as rss
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from datetime import datetime
from flask_jsonpify import jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['RSS_FOLDER'] = rss.RSS_FOLDER
api = Api(app)

def parsehtml(content):
    html = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1.0"/><meta http-equiv="X-UA-Compatible" content="ie=edge"/><title>RSS</title></head><body>'+content+'</body></html>'
    return html

@app.route("/rssinput", methods=['POST'])
def rssinput():
    link = request.form['link']
    title = request.form['title']
    description = title
    rss.append(link, title, description)
    return redirect(url_for('rssfeed'))

@app.route("/rssfeed")
def rssfeed():
    return send_from_directory(app.config['RSS_FOLDER'],'rss.xml')

@app.route("/input")
def input():
    link = '<label>Link</label><input type="text" name="link" required/><br>'
    description = '<label>Description(optional)</label><input type="text" name="description"/><br>'
    title = '<label>Title(optional)</label><input type="text" name="title" required/><br>'
    return parsehtml('<form action="/rssinput" method="post" >'+title+link+'<input type="submit">Submit</input></form>') 

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host= 'localhost', port=5005)