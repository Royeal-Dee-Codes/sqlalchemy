import uuid

import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID

from db import db


class AppUsers(db.Model):
    __tablename__ = "AppUsers"

    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def new_user_obj():
        return AppUsers("", "")


class AppUsersSchema(ma.Schema):
    class Meta:
        fields = ['user_id', 'email']


app_user_schema = AppUsersSchema()
app_users_schema = AppUsersSchema(many=True)
