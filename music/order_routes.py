from flask import Blueprint, request, jsonify
from . import db
from .models import Order, Customer
from .serializer import order_schema, order_schemas

order = Blueprint('order', __name__, url_prefix='/api/v1')

# create orders related to each customers
@order.route("/customers/<int:customer_id>/orders", methods=['POST'])
def create_order(customer_id):
    data = request.get_json()
    #filled = data['filled']
    order_description = data['order_description']
    new_order = Order(customer_id=int(customer_id), **data)
    db.session.add(new_order)
    db.session.commit()
    result = order_schema.dump(new_order)
    return jsonify(result)

# get all orders related to each customers
@order.route("/customers/<int:customer_id>/orders", methods=['GET'])
def get_all_customer_order(customer_id):
    data = Order.query.filter_by(customer_id=int(customer_id))
    for order in data:
        mylist = []
        result = order_schema.dump(order)
        mylist.append(result)
    return jsonify(mylist)
