from rest_api_demo.database import db
from rest_api_demo.database.models import User


def create_blog_user(data):
    username = data.get('username')
    email = data.get('email')
    user = User(username, email)
    db.session.add(user)
    db.session.commit()

