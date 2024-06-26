from flask import jsonify, Request, request

from db import db
from models.products import Products, products_schema, product_schema
from util.reflection import populate_object


def product_add(req):
    post_data = req.form if req.form else req.get_json()

    new_product = Products.new_product_obj()
    populate_object(new_product, post_data)

    try:
        db.session.add(new_product)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400

    return jsonify({"message": "product created", "result": product_schema.dump(new_product)}), 201


def products_get_all():
    products_query = db.session.query(Products).all()

    print(products_query)

    return jsonify({"message": "products found", "results": products_schema.dump(products_query)}), 200


def product_get_by_id(product_id):
    product_query = db.session.query(Products).filter(Products.product_id == product_id).first()

    if not product_query:
        return jsonify({"message": "product not found"}), 404

    # category_list = []

    # for category in product_query.categories:
    #     category_list.append({
    #         'category_id': category.category_id,
    #         'category_name': category.category_name
    #     })

    # company_dict = {
    #     'company_id': product_query.company.company_id,
    #     'compnay_name': product_query.company.company_name
    # }

    # if product_query.warranty:
    #     warranty_dict = {
    #         'warranty_id': product_query.warranty.warranty_id,
    #         'warranty_month': product_query.warranty.warranty_months
    #     }

    # else:
    #     warranty_dict = {}

    # product_dict = {
    #     'product_id': product_query.product_id,
    #     'product_name': product_query.product_name,
    #     'description': product_query.description,
    #     'price': product_query.price,
    #     'active': product_query.active,
    #     'company': company_dict,
    #     'warranty': warranty_dict,
    #     'categories': category_list
    # }

    return jsonify({"message": "product found", "results": product_schema.dump(product_query)}), 200


def product_category_add(req, product_id):
    post_data = req.form if req.form else req.json()

    # product_id = post_data.get('product_id')
    # category_id = post_data.get('category_id')

    # product_query = db.session.query(Products).filter(Products.product_id == product_id).first()
    # category_query = db.session.query(Categories).filter(Categories.category_id == category_id).first()
    new_product = Products.new_product_obj()
    populate_object(new_product, post_data)

    try:
        db.session.add(new_product)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update record"}), 400

    return jsonify({"message": "product created", "result": products_schema.dump(new_product)}), 201


def products_get_all():
    products_query = db.session.query(Products).all()

    print(products_query)

    return jsonify({"message": "products found", "results": products_schema.dump(products_query)}), 200


def product_get_by_id(product_id):
    product_query = db.session.query(Products).filter(Products.product_id == product_id).first()

    if not product_query:
        return jsonify({"message": f"product does not exist"}), 400

    return jsonify({"message": "product found", "result": product_schema.dump(product_query)}), 200


def product_update(req, product_id):
    post_data = req.form if req.form else req.json

    product_query = db.session.query(Products).filter(Products.product_id == product_id).first()

    populate_object(product_query, post_data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update record"}), 400

    return jsonify({"message": "product updated", "result": product_schema.dump(product_query)}), 200


def product_delete(product_id):
    product_query = db.session.query(Products).filter(Products.product_id).first()

    if not product_query:
        return jsonify({"message": f"product {product_id} does not exist"}), 404

    try:
        db.session.delete(product_query)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete"}), 400

    return jsonify({"message": "product delelted", "result": product_schema.dump(product_query)}), 200
