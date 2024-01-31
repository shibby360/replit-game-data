from flask import Flask, request
import skuv
import textvil

app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

#skuv
@app.route('/skuv/save', methods=['POST'])
def skuvsavepost():
  return skuv.savepost(request)
@app.route('/skuv/getdata', methods=['GET'])
def skuvgetdata():
  return skuv.getdata(request)

#text village
@app.route('/text-vil/makeacc', methods=['GET'])
def textvilmakeacc():
  return textvil.makeacc(request)
@app.route('/text-vil/data', methods=['GET'])
def textvilgetdata():
  return textvil.getdata(request)
@app.route('/text-vil/save', methods=['POST'])
def textvilsaveroute():
  return textvil.saveroute(request)
@app.route('/text-vil/newid', methods=['GET'])
def textvilnewid():
  return textvil.newid()
@app.route('/text-vil/delid/<dlid>')
def textvildelid(dlid):
  return textvil.delid(dlid)
@app.route('/text-vil/attackname', methods=['GET'])
def textvillageattackname():
  return textvil.attackname(request)
if __name__ == '__main__':
  app.run(host='0.0.0.0')