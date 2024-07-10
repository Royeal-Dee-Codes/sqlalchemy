from flask import jsonify, request
from flask_bcrypt import generate_password_hash

from db import db
from models.app_users import AppUsers, app_user_schema, app_users_schema
from util.reflection import populate_object


def user_add(request):
    post_data = request.form if request.form else request.json

    new_user = AppUsers.new_user_obj()

    populate_object(new_user, post_data)

    new_user.password = generate_password_hash(new_user.password).decode('utf8')

    try:
        db.session.add(new_user)
        db.session.commit()

    except:
        db.session.rollback()
        return jsonify({"message": "unable to create user"}), 400

    return jsonify({"message": "user created", "results": app_user_schema.dump(new_user)}), 201
