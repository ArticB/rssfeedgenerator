import uuid
import pymongo
from lxml import etree as ET    
from bson.objectid import ObjectId
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["RSS"]

def add_new_file(_title, _filename):
    new = db["RSS_file"]
    title = _title
    filename = _filename
    print(title, filename)
    new_id = new.insert_one({
        'title':title,
        'filename':filename
    })

def get_all_file():
    new = db["RSS_file"]
    result = new.find()
    l=[]
    for i in result:
        i["_id"] = str(i["_id"])
        l.append(i) 
    return l

def find_one_file(id):
    new = db["RSS_file"]
    result = new.find_one({'_id': ObjectId(id)})
    return result

def delete_one(id):
    new = db["RSS_file"]

    try:
        query = {'_id':ObjectId(id)}
        new.delete_one(query)
        return "done"
    except:
        return "error"

def getfilename(id):
    new = db["RSS_file"]

    try:
        query={'_id':ObjectId(id)}
        result = new.find_one(query)
        return result['filename']
    except:
        return "error"
