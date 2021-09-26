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
