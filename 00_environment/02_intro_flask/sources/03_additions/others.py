@app.route(api_url+'/users/<string:username>',methods=['GET'])
def read_one_user(username):
   return username, 200

@app.route(api_url+'/users/<string:username>/commands',methods=['GET'])
def read_commands(username):
   return username, 200

# 192.168.57.2:8080/v1.0/users/recently_logged?time=5mi&group=root
@app.route(api_url+'/users/recently_logged',methods=['GET'])
def read_user_filter():
   time  = request.args.get("time")
   group = request.args.get("group")
   return group, 200
