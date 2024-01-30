import re
from flask import Flask, request
import string
import json, random as rand
class idgen:
  def gen(debug=False):
    end = ''
    while end in db['ids']:
      end = ''
      rnge = rand.randint(15, 25)
      for i in range(rnge):
        end += rand.choice(string.digits + string.ascii_letters)
    if not debug:
      db['ids'].append(end)
    return end


app = Flask('app')
def addattr(attr, val):
  for i in db:
    if i == 'ids':
      continue
    db[i][attr] = val

for i in db:
  print(i, db.get_raw(i), sep=': ', end='\n\n')
@app.route('/')
def hello_world():
  return 'Bonjour, le monde!'

@app.route('/wakeup')
def wakeup():
  return 'im waking up'

@app.route('/makeacc')
def makeacc():
  uid = idgen.gen()
  bdgid = idgen.gen()
  db[uid] = {
    'username':request.form['username'],
    'password':request.form['password'],
    'coins':0,
    'buildings':{bdgid:{'type':'village hall', 'level':1, 'x':0, 'y':0, 'dead':False}},
    'troops':{}
  }
  return {uid:json.loads(db.get_raw(uid))}

@app.route('/data', methods=['GET', 'POST'])
def getdata():
  unm = request.form['username']
  pwd = request.form['password']
  unms = []
  for i in db:
    if i == 'ids':
      continue
    if db[i]['username'] == unm and db[i]['password'] == pwd:
      return {i:json.loads(db.get_raw(i))}
  return {'msg':'incorrect'}

@app.route('/save', methods=['POST'])
def saveroute():
  uid = request.form['userid'][::-1]
  userdata = json.loads(request.form['userdata'])
  if 'password' not in userdata:
    userdata['password'] = json.loads(db.get_raw(uid))['password']
  # db[uid] = userdata
  print(userdata)
  return 'success'

@app.route('/newid')
def newid():
  uid = idgen.gen()
  return uid

@app.route('/delid/<dlid>')
def delid(dlid):
  db['ids'].remove(dlid)
  return 'success'

@app.route('/attackname')
def attackname():
  randomid = rand.choice(list(db.keys()))
  while randomid == request.form['userfrom'] or randomid == 'ids':
    randomid = rand.choice(list(db.keys()))
  newdc = json.loads(db.get_raw(randomid)).copy()
  del newdc['password']
  newdc['uid'] = randomid
  return newdc

app.run(host='0.0.0.0', port=8080)
