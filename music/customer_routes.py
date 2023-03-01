from flask import jsonify, request, Blueprint, abort
from .serializer import customer_schema, customer_schemas
from . import db
from .models import Customer

customer = Blueprint('customer', __name__, url_prefix='/api/v1')

# get all customers
@customer.route('/customers/', methods=['GET'])
def all_customers():
    data = Customer.query.all()
    if request.method != "GET":
        abort(405)
    if not data:
        abort(404)
    result = customer_schemas.dump(data)
    return jsonify(result), 200

# create a customer
@customer.route('/customers/')
@customer.route('/customers', methods=['POST'])
def create_customers():
    data = request.get_json()
    new_customer = Customer(**data)
    db.session.add(new_customer)
    db.session.commit()
    result = customer_schema.dump(new_customer)
    return jsonify(result), 201

# get specific customer
@customer.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    data = Customer.query.get(int(customer_id))
    if not data:
        abort(404, "No such customer")
    
    if request.method != 'GET':
        abort(405)
    
    result = customer_schema.dump(data)
    return jsonify(result), 200

@customer.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    data = Customer.query.filter_by(id=int(customer_id)).first()
    db.session.delete(data)
    db.session.commit()
    return jsonify({"message": "Deleted"})

@customer.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = Customer.query.get(int(customer_id))
    email = request.get_json()['email']
    username = request.get_json()['username']
    password = request.get_json()['password']
    
    data.email = email
    data.username = username
    data.password = password
    db.session.commit()

    result = customer_schema.dump(data)
    return jsonify(result)