from flask_restplus import fields
from rest_api_demo.api.restplus import api

blog_user = api.model('Blog user', {
    'username': fields.String(required=True, description='User username'),
    'email': fields.String(required=True, description='User email address'),
})
