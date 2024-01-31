from flask import Flask, request
import skuv

app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/skuv/save', methods=['POST'])
def skuvsavepost():
  return skuv.savepost(request)

@app.route('/skuv/getdata', methods=['GET'])
def skuvgetdata():
  return skuv.getdata(request)

if __name__ == '__main__':
  app.run(host='0.0.0.0')