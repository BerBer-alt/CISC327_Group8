from qbay import app
from flask_sqlalchemy import SQLAlchemy

'''
This file defines data models and related business logics
'''


db = SQLAlchemy(app)


# the class for transaction objects
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), unique=True, nullable=False)
    product_id = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Integer, unique=False, nullable=False)
    date = db.Column(db.String(10), unique=False, nullable=False)

    def __repr__(self):
        return "<Transaction %r>" % self.id


# the class for product objects
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=True)
    description = db.Column(db.String(2000), unique=False, nullable=False)
    price = db.Column(db.Integer, unique=False, nullable=False)
    last_modified_date = db.Column(db.String(10), unique=False, nullable=False)
    owner_email = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return "<Product %r>" % self.id


# create all tables
db.create_all()


def create_product(title, description, price, last_modified_date, owner_email):
    """
    Create a new product.
      Parameters:
        title:               title
        description:         description
        price:               price
        last_modified_date:  last_modified_date
        owner_email:         owner_email
      Returns:
        True if creation succeeded otherwise False.
    """
    # check if the title of the product is not alphanumeric-only,
    # and space allowed only
    if not(all(c.isalnum() or c.isspace() for c in title)):
        return False
    # check if prefix or suffix has space
    if (len(title) != 0) and (title[0] == ' ') or (title[-1] == ' '):
        return False
    # check if the title has more than 80 characters
    if len(title) > 80:
        return False
    # check if the length of description is less than 20 characters
    # or more than 2000 characters
    if (len(description) < 20) | (len(description) > 2000):
        return False
    # check if the length of description is less than the length of title
    if len(description) < len(title):
        return False
    # check if the price is less than 10 or more than 10000
    if (price < 10) | (price > 10000):
        return False
    # check if the last modified date is before 2021-01-02 or after 2025-01-02
    if last_modified_date < '2021-01-02':
        return False
    if last_modified_date > '2025-01-02':
        return False
    # check if owner email is empty,
    # and the owner does not exist in the database
    if owner_email == '':
        return False
    # check if the product has the same title
    existed = Product.query.filter_by(title=title).all()
    if len(existed) > 0:
        return False

    # create a new product
    product = Product(id=db.session.query(Product).count() + 1, title=title,
                      description=description, price=price,
                      last_modified_date=last_modified_date,
                      owner_email=owner_email)
    # add it to the current database session
    db.session.add(product)
    # actually save the product object
    db.session.commit()

    return True
