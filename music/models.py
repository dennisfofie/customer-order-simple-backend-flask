from . import db
from datetime import datetime
from uuid import uuid4

#creates models [Customer]
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(600))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    city = db.Column(db.String(100))
    street = db.Column(db.String(200))
    zip_code = db.Column(db.Integer)
    order = db.relationship('Order', backref='customer')

    def __repr__(self) -> str:
        return f"<Customer> {self.id} {self.username}"

#create models [Order]
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_description = db.Column(db.Text)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    filled = db.Column(db.Boolean, default=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))


    def __repr__(self) -> str:
        return f"<Order> {self.id} {self.order_number}"




