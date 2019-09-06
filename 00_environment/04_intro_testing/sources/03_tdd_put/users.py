from flask import Flask

app = Flask(__name__)
api_url = '/v1.0'

@app.route(api_url+'/users',methods=['PUT'])
def update_user():
  return "not implemented", 501

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8088,debug='True')
