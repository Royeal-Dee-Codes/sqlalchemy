from flask import request, Blueprint

import controllers

product = Blueprint('product', __name__)


@product.route('/product', methods=['POST'])
def product_add():
    return controllers.product_add(request)


@product.route('/product/<product_id>', methods=['GET'])
def product_get_by_id(product_id):
    return controllers.product_get_by_id(product_id)


@product.route('/products', methods=['GET'])
def get_all_products():
    return controllers.get_all_products(request)


@product.route('/product/category', methods=['POST'])
def product_category_add():
    return controllers.create_product_category(request)


@product.route('/product/<product_id>', methods=['PUT'])
def update_product(product_id):
    return controllers.update_product(request, product_id)
