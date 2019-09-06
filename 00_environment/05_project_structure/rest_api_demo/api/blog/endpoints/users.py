import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.blog.business import create_blog_user
from rest_api_demo.api.blog.serializers import blog_user
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import User

log = logging.getLogger(__name__)

ns = api.namespace('blog/users', description='Operations related to blog users')


@ns.route('/')
@api.response(404, 'User not found.')
class Users(Resource):

    @api.response(200, 'User found.')
    @api.marshal_with(blog_user)
    def get(self):
        users = User.query.all()
        log.info('{}'.format(users))
        return users

    @api.response(200, 'User created.')
    @api.expect(blog_user)
    def post(self):
        create_blog_user(request.json)
        return None, 201
