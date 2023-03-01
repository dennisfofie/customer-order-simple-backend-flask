from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


#instantiate db
db = SQLAlchemy()
ma = Marshmallow()

# instantiate a new flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']= 'This is my secret key for testing'
db.init_app(app)
ma.init_app(app)

"""register blueprint"""
from .customer_routes import customer
from .order_routes import order
app.register_blueprint(customer)
app.register_blueprint(order)