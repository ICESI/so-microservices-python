from flask import Flask
import json
from user_commands import get_all_users, add_user, remove_user
app = Flask(__name__)
api_url = '/v1.0'

@app.route(api_url+'/users',methods=['POST'])
def create_user():
  return "not implemented", 501

@app.route(api_url+'/users',methods=['GET'])
def read_user():
  return "not implemented", 501

@app.route(api_url+'/users',methods=['PUT'])
def update_user():
  return "not implemented", 501

@app.route(api_url+'/users',methods=['DELETE'])
def delete_user():
  return 'not implemented', 501

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8088,debug='True')
