import re
import string
import json, random as rand
import os
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
if os.path.isfile('mongouri.txt'):
  connectionstring = open('mongouri.txt').read().strip()
else:
  connectionstring = os.environ.get('MONGO_URI')
cluster = pymongo.MongoClient(connectionstring)
database = cluster['replit-text-games']
data = database['text-vil']
objid = ObjectId('65b9da692c4a8ee403f13743')
doc = data.find_one({'_id':objid})
del doc['_id']
db = doc

def addattr(attr, val):
  for i in db:
    if i == 'ids':
      continue
    db[i][attr] = val

def makeacc(request):
  uid = idgen.gen()
  bdgid = idgen.gen()
  db[uid] = {
    'username':request.form['username'],
    'password':request.form['password'],
    'coins':0,
    'buildings':{bdgid:{'type':'village hall', 'level':1, 'x':0, 'y':0, 'dead':False}},
    'troops':{}
  }
  return {uid:db[uid]}

def getdata(request):
  unm = request.form['username']
  pwd = request.form['password']
  unms = []
  for i in db:
    if i == 'ids':
      continue
    if db[i]['username'] == unm and db[i]['password'] == pwd:
      return {i:db[i]}
  return {'msg':'incorrect'}

def saveroute(request):
  uid = request.form['userid'][::-1]
  userdata = json.loads(request.form['userdata'])
  if 'password' not in userdata:
    userdata['password'] = db[uid]['password']
  # db[uid] = userdata
  print(userdata)
  return 'success'

def newid():
  uid = idgen.gen()
  return uid

def delid(dlid):
  db['ids'].remove(dlid)
  return 'success'

def attackname(request):
  randomid = rand.choice(list(db.keys()))
  while randomid == request.form['userfrom'] or randomid == 'ids':
    randomid = rand.choice(list(db.keys()))
  newdc = db[randomid].copy()
  del newdc['password']
  newdc['uid'] = randomid
  return newdc