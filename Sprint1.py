from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

# class for shipping after transaction
class  shipping(db.Model):
    shipping_id = db.Column(db.Integer, primary_key=True)
    shipping_contact = db.Column(db.Integer, primary_key=True)
    shipping_company = db.Column(db.String(80), unique=False, nullable=False)
    shipping_sender = product_name = db.Column(db.String(80), unique=False, nullable=False)
    shipping_receiver = product_name = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return "<Shipping %r>" % self.shipping_id