from flask import Flask

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def read_user():
  return 'read all users'

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8080)
