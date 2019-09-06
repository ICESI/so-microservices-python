from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from rest_api_demo.database.models import User  # noqa
    db.drop_all()
    db.create_all()
