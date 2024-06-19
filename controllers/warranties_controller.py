from flask import jsonify

from db import db
from models.warranties import Warranties, warranties_schema, warranty_schema
from util.reflection import populate_object


def warranty_add(req):
    post_data = req.form if req.form else req.get_json()

    new_warranty = Warranties.new_warranty_obj()
    populate_object(new_warranty, post_data)

    try:
        db.session.add(new_warranty)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400

    return jsonify({"message":
                    "warranty created", "result": warranties_schema.dump(new_warranty)}), 201


def warranties_get_all():
    warranties_query = db.session.query(Warranties).all()

    print(warranties_query)

    return jsonify({"message": "warranties found", "results": warranties_schema.dump(warranties_query)}), 200


def warranty_get_by_id(warranty_id):
    warranties_query = db.session.query(Warranties).filter(Warranties.warranty_id == warranty_id).first()
    if not warranties_query:
        return jsonify({"message": "warranty found", "result": warranties_schema.dump(warranties_query)}), 400

    return jsonify({"message": "warranty found", "result": warranty_schema.dump(warranties_query)}), 200


def warranty_update(req, warranty_id):
    post_data = req.form if req.form else req.json

    warranty_query = db.session.query(Warranties).filter(Warranties.warranty_id == warranty_id).first()

    populate_object(warranty_query, post_data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update warranty"}), 400

    return jsonify({"message": "warranty updated", "results": warranty_schema.dump(warranty_query)}), 200


def warranty_delete(warranty_id):
    warranty_query = db.session.query(Warranties).filter(Warranties.warranty_id).first()

    if not warranty_query:
        return jsonify({"message": f"warranty {warranty_id} does not exist"}), 404

    try:
        db.session.delete(warranty_query)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete"}), 400

    return jsonify({"message": "warranty deleted", "results": warranty_schema.dump(warranty_query)}), 200
