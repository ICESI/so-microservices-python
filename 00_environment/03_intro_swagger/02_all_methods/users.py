import json
from flask import Flask, abort, request
from flask_restplus import Resource, Api
from flask_restplus import fields

from users_commands import get_all_users, add_user, remove_user

app = Flask(__name__)
#api = Api(app)
api = Api(app,version='1.0', title='API for users management', description='A demonstration of a Flask RestPlus powered API')

os_user = api.model('User', {
    'username': fields.String(required=True, description='username to be created', example='operativos'),
    'password': fields.String(required=True, description='password for the username', example='mysecurepass'),
})

ns = api.namespace('v1.0/users', description='Operations related to create users')

@ns.route('/')
#@api.route(api_url+'/users')
class UserCollection(Resource):
    @api.response(200, 'List of users successfully returned.')
    def get(self):
        """ returns a list of users """
        list = {}
        list["users"] = get_all_users()
        return json.dumps(list), 200

    @api.response(201, 'User successfully created.')
    @api.expect(os_user)
    def post(self):
        """ creates a user """
        content = request.get_json(silent=True)
        username = content['username']
        password = content['password']
        if not username or not password:
            return "empty username or password", 400
        if username in get_all_users():
            return "user already exist", 400
        if add_user(username,password):
            return "user created", 201
        else:
            return "error while creating user", 400

    @api.response(501, 'Not implemented.')
    def put(self):
        """ not implemented """
        return "not implemented", 501 # Not found

    @api.response(201, 'All users were deleted.')
    @api.response(400, 'Some users were not deleted.')
    def delete(self):
        """ deletes a user """
        error = False
        for username in get_all_users():
            if not remove_user(username):
                error = True
                if error:
                    return 'some users were not deleted', 400
                else:
                    return 'all users were deleted', 200

# @ns.route('/<int:id>')
# @api.response(404, 'Category not found.')
# class UserItem(Resource):
#     def get(self,id):
#         """ returns details of a user """
#         return "not implemented", 501

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8088,debug='True')
