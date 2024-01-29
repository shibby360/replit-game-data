from flask import Flask, request
import json
from replit import db
app = Flask('app')
print(dict(db))
def addkeytoall(key, val):
  for i in db:
    db[i][key] = val

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/alarmclockisgoingwakeup')
def alarmclockisgoingwakeup():
  return 'ok geez'
  
@app.route('/save', methods=['POST'])
def savepost():
  userdata = json.loads(request.form['userdata'])
  userid = request.args['userid'][::-1]
  db[userid] = userdata
  return 'saved'

@app.route('/getdata', methods=['GET'])
def getdata():
  enddb = {}
  for key in dict(db):
    enddb[key] = json.loads(db.get_raw(key))
  return enddb
