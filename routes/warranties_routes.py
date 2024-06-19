from flask import request, Blueprint

import controllers

warranty = Blueprint('warranty', __name__)


@warranty.route('/warranty', methods=['POST'])
def warranty_add():
    return controllers.warranty_add(request)


@warranty.route('/warranty/<warranty_id>', methods=['GET'])
def warranty_get_by_id(warranty_id):
    return controllers.warranty_get_by_id(warranty_id)


@warranty.route('/warranties', methods=['GET'])
def warranties_get_all():
    return controllers.warranties_get_all(request)


@warranty.route('/warranty/<warranty_id>', methods=['PUT'])
def warranty_update(warranty_id):
    return controllers.warranty_update(request, warranty_id)
