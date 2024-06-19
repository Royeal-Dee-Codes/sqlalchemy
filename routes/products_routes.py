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
def products_get_all():
    return controllers.products_get_all(request)


@product.route('/product/category', methods=['POST'])
def product_category_add():
    return controllers.create_product_category(request)


@product.route('/product/<product_id>', methods=['PUT'])
def product_update(product_id):
    return controllers.product_update(request, product_id)
