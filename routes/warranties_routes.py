from flask import request, Blueprint

import controllers

warranties = Blueprint('warranty', __name__)


@warranties.route('/warranty', methods=['POST'])
def warranty_add():
    return controllers.warranty_add(request)


@warranties.route('/warranty/<warranty_id>', methods=['GET'])
def warranty_get_by_id(warranty_id):
    return controllers.warranty_get_by_id(warranty_id)


@warranties.route('/warranties', methods=['GET'])
def warranties_get_all():
    return controllers.warranties_get_all(request)


@warranties.route('/warranty/<warranty_id>', methods=['PUT'])
def warranty_update(warranty_id):
    return controllers.warranty_update(request, warranty_id)
