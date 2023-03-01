from .models import Customer, Order
from . import ma

class CustomerSchema(ma.Schema):
    class Meta:
        model = Customer
        fields = ('id', 'username', 'first_name', 'email', 'created_at')


# schema instances
customer_schema = CustomerSchema(many=False)
customer_schemas = CustomerSchema(many=True)

class OrderSchema(ma.Schema):
    class Meta:
        model = Order
        fields = ('id','order_description', 'filled', 'customer_id', 'order_number', 'order_date' )

# order schema instances
order_schema = OrderSchema(many=False)
order_schemas = OrderSchema(many=True)