from flask import request, Blueprint

import controllers

products = Blueprint('products', __name__)


@products.route('/product', methods=['POST'])
def product_add():
    return controllers.product_add(request)


@products.route('/product/<product_id>', methods=['GET'])
def product_get_by_id(product_id):
    return controllers.product_get_by_id(product_id)


@products.route('/products', methods=['GET'])
def products_get_all():
    return controllers.products_get_all(request)


@products.route('/product/category', methods=['POST'])
def product_category_add():
    return controllers.create_product_category(request)


@products.route('/product/<product_id>', methods=['PUT'])
def product_update(product_id):
    return controllers.product_update(request, product_id)
