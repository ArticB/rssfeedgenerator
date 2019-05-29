import db
import os
import rssgenerator as rss
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from datetime import datetime
from flask_jsonpify import jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['RSS_FOLDER'] = rss.RSS_FOLDER
api = Api(app)
CORS(app)
def parsehtml(content):
    html = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1.0"/><meta http-equiv="X-UA-Compatible" content="ie=edge"/><title>RSS</title></head><body>'+content+'</body></html>'
    return html

# @app.route("/rssinput", methods=['POST'])
# def rssinput():
#     link = request.form['link']
#     title = request.form['title']
#     description = title
#     rss.append(link, title, description)
#     return redirect(url_for('rssfeed'))

# @app.route("/input")
# def input():
#     link = '<label>Link</label><input type="text" name="link" required/><br>'
#     description = '<label>Description(optional)</label><input type="text" name="description"/><br>'
#     title = '<label>Title(optional)</label><input type="text" name="title" required/><br>'
#     return parsehtml('<form action="/rssinput" method="post" >'+title+link+'<input type="submit">Submit</input></form>') 

@app.route("/createnewrss", methods=['POST'])
def createnewrss():
    title = request.form['title']
    try:
        uuid = rss.generate_new_rss(title)
        db.add_new_file(title, uuid)
        return jsonify({"message":"done"}), 200
    except:
        return jsonify({"error":"error"}), 400
    
@app.route("/createnewitem", methods=['POST'])
def createnewitem():
    title = request.form['title']
    link = request.form['link']
    _id = request.form['_id']
    description = title
    filename = db.getfilename(_id)
    try:
        rss.append(link, title, description, filename)
        return jsonify({"message":"done"}), 200
    except:
        return jsonify({"message":"error"}), 400
    

@app.route("/rssfeed/<id>")
def rssfeed(id):
    filepath = db.getfilename(id)
    print(filepath)
    return send_from_directory(app.config['RSS_FOLDER'],filepath+'.xml')

     
@app.route("/getall", methods=['POST'])
def getallitems():
    _option = request.form['option'] 
    if _option == 'items':            
        _id = request.form['_id']
        _filename = db.getfilename(_id)
        _alldata = rss.get_all_items(_filename)
        return jsonify({'template' : render_template('tbody.html', alldata =_alldata, option =_option), 'alldata':_alldata})
    else:
        _alldata = db.get_all_file()
        return jsonify({'template' : render_template('tbody.html', alldata=_alldata, option = _option), 'alldata':_alldata})
   
@app.route("/geta", methods=['POST'])
def geta():
    id = request.form['_id']
    return jsonify({'template' : render_template('a.html', _id=id)})
        
@app.route("/")  
def hello():
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(host= 'localhost', port=5000)