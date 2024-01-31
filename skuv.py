import pymongo
from bson.objectid import ObjectId
import json
import os
if os.path.isfile('mongouri.txt'):
  connectionstring = open('mongouri.txt').read().strip()
else:
  connectionstring = os.environ.get('MONGO_URI')
cluster = pymongo.MongoClient(connectionstring)
database = cluster['replit-text-games']
data = database['sk-uv']
objid = ObjectId('65b731e556fdaed03a736e72')
doc = data.find_one({'_id':objid})
del doc['_id']
db = doc
def addkeytoall(key, val):
  for i in db:
    db[i][key] = val
def save():
  data.update_one({'_id':objid}, {'$set':db})

def savepost(request):
  userdata = json.loads(request.form['userdata'])
  userid = request.args['userid'][::-1]
  db[userid] = userdata
  save()
  return 'saved'

def getdata(request):
  enddb = {}
  for key in dict(db):
    enddb[key] = db[key]
  save()
  return enddb