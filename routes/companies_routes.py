from flask import request, Blueprint

from controllers import companies_controller

companies = Blueprint('companies', __name__)


@companies.route('/company', methods=['POST'])
def companies_add():
    return companies_controller.company_add(request)


@companies.route('/companies')
def companies_get_all():
    return companies_controller.companies_get_all()


@companies.route('/company/<company_id>', methods=["GET"])
def companies_get_by_id(company_id):
    return companies_controller.company_get_by_id(company_id)


@companies.route('/company/<company_id>', methods=['PUT'])
def company_update(company_id):
    return companies_controller.company_update_by_id(request, company_id)


@companies.route('/companies/delete/<company_id>', methods=['DELETE'])
def company_delete(company_id):
    return companies_controller.company_delete(company_id)
