from flask import Flask
from user_commands import get_all_users
import json

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def read_user():
  list = {}
  list["users"] = get_all_users()
  return json.dumps(list), 200

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8080)
