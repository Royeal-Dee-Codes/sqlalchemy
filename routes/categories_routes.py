from flask import request, Blueprint

import controllers

categories = Blueprint('categories', __name__)


@categories.route('/category', methods=['POST'])
def category_add():
    return controllers.category_add(request)


@categories.route('/categories')
def categories_get_all():
    return controllers.categories_get_all()


@categories.route('/categories/<category_id>', methods=['GET'])
def categories_get_by_id(category_id):
    return controllers.category_get_by_id(category_id)


@categories.route('/categories/<category_id>', methods=['PUT'])
def category_update(category_id):
    return controllers.category_update(request, category_id)


@categories.route('/categories/delete/<category_id>', methods=['DELETE'])
def category_delete(category_id):
    return controllers.category_delete(category_id)
