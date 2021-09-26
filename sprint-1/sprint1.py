from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


# Users' balance is added here
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # balance of the user
    balance = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username


# the class for product objects
class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(80), unique=False, nullable=False)
    product_price = db.Column(db.Integer, nullable=False)
    product_seller_id = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return "<Product %r>" % self.product_id


# class for shipping after transaction
class shipping(db.Model):
    shipping_id = db.Column(db.Integer, primary_key=True)
    shipping_contact = db.Column(db.Integer, primary_key=True)
    shipping_company = db.Column(db.String(80), unique=False, nullable=False)
    shipping_sender = product_name = db.Column(
        db.String(80), unique=False, nullable=False)
    shipping_receiver = product_name = db.Column(
        db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return "<Shipping %r>" % self.shipping_id


# the class for Review objects
class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    buyer_username = db.Column(db.String(80), unique=True, nullable=False)
    seller_username = db.Column(db.String(80), unique=True, nullable=False)
    comment = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Review %r>' % self.review_id


# the class for transaction objects
class transaction(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True)
    transaction_product_id = db.Column(db.Integer, unique=True, nullable=False)
    transaction_price_id = db.Column(db.Integer, unique=True, nullable=False)
    transaction_buyer_id = db.Column(db.Integer, unique=True, nullable=False)
    transaction_seller_id = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return "<Transaction %r>" % self.transaction_id
