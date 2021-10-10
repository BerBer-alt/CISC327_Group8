from qbay import app
from flask_sqlalchemy import SQLAlchemy
import re
from datetime import datetime


db = SQLAlchemy(app)


# the class for user objects
class User(db.Model):
    username = db.Column(
        db.String(80), nullable=False)
    email = db.Column(
        db.String(120), unique=True, nullable=False,
        primary_key=True)
    password = db.Column(
        db.String(120), nullable=False)
    shipping_address = db.Column(
        db.String(120), unique=False, nullable=True,
        primary_key=False)
    postal_code = db.Column(
        db.String(120), unique=False, nullable=True,
        primary_key=False)
    balance = db.Column(
        db.Integer,
        unique=False,
        nullable=True,
        primary_key=False)

    def __repr__(self):
        return '<User %r>' % self.username


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


# the class for review objects
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(
        db.String(120), unique=True, nullable=False)
    score = db.Column(db.Integer, unique=True, nullable=False)
    review_text = db.Column(db.String(500), unique=False, nullable=False)

    def __repr__(self):
        return '<Review %r>' % self.review_id


# create all tables
db.create_all()


# this function check if the Email address inputed fits the format or not
def check_Email(Input_str: str):
    if Input_str == "":
        return False
    regex = r"(^[a-zA-Z0-9_.+-/!#$%&'*/=?^_`{|}~\" ]" \
            r"+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if re.search(regex, Input_str) is None:
        return False
    domain = Input_str[0:Input_str.index("@")]
    if domain[0] == "." or domain[-1] == ".":
        return False
    if domain.find("\"") != -1:
        fir_q = domain.find("\"")
        sec_q = domain.find("\"", fir_q + 1)
        if sec_q == -1:
            return False
        domain = domain[0:fir_q] + domain[sec_q + 1:]
        if domain.find(".") == -1 and fir_q != 0 and sec_q != len(Input_str):
            return False
    if domain.find("..") != -1 or domain.find(" ") != -1:
        return False

    return True


# this function check the string that input fits the requirnment or not
def check_Password(Input_password: str):
    if Input_password.__len__() < 6:
        return False
    Flag_upper = False
    Flag_lower = False
    Flag_Spec = False
    for i in Input_password:
        if i.isupper():
            Flag_upper = True
        elif i.islower():
            Flag_lower = True
        elif i in "!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~":
            Flag_Spec = True
    return Flag_Spec and Flag_lower and Flag_upper


# this function check the input string fits the user requirnment or not
def check_Username(Input_Username: str):
    if Input_Username.__len__() <= 2 or Input_Username.__len__() > 20:
        return False
    if Input_Username[0] == " " or Input_Username[-1] == " ":
        return False
    for i in Input_Username:
        if not i.isalnum():
            return False
    return True


# functino used to register
def register(name, email, password):
    '''
    Register a new user
      Parameters:
        name (string):     user name
        email (string):    user email
        password (string): user password
      Returns:
        True if registration succeeded otherwise False
    '''

    if not check_Username(name):
        return False
    if not check_Email(email):
        return False
    if not check_Password(password):
        return False

    # check if the email has been used:
    existed = User.query.filter_by(email=email).all()
    if len(existed) > 0:
        return False

    # create a new user
    user = User(
        username=name,
        email=email,
        password=password,
        # Shipping address is empty at the time of registration
        shipping_address="",
        # Postal code is empty at the time of registration
        postal_code="",
        balance=100)        # free $100 dollar signup bonus
    # add it to the current database session
    db.session.add(user)
    # actually save the user object
    db.session.commit()

    return True


# function used to login
def login(email, password):
    '''
    Check login information
      Parameters:
        email (string):    user email
        password (string): user password
      Returns:
        The user object if login succeeded otherwise None
    '''

    if not check_Email(email):
        return None
    if not check_Password(password):
        return None
    valids = User.query.filter_by(email=email, password=password).all()
    if len(valids) != 1:
        return None
    return valids[0]


# creating product and give it with relative information
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


# using email to find account and update user information
def update_profile(email, name, shipping_address, postal_code):
    '''
    Update user profile
      Parameters:
        name (string):              user name
        shipping_address (string):  shipping address
        postal_code (string):       postal code
      Returns:
        Boolean value, true for successful update otherwise update fails
    '''

    # shipping address should not be empty or contain no special charactors
    if (not(shipping_address) or
            (shipping_address.isalnum() is False)):
        return False
    # Canadian zip code configuration
    if not((len(re.findall(
        r'[A-Z]{1}[0-9]{1}[A-Z]{1}\s*[0-9]{1}[A-Z]{1}[0-9]{1}',
            postal_code.upper()))) == 1):
        return False
    # user name should not empty and not space at prefix or suffix
    if (not(name) or len(name) >= 20 or len(name) <= 2 or
        name[0] == " " or
        name[-1] == " " or
            not(all(i.isalnum() or i.isspace() for i in name))):
        return False

    # overwrite each attribute of the product
    user = User.query.filter_by(email=email).first()
    user.name = name
    user.postal_code = postal_code
    user.shipping_address = shipping_address
    db.session.commit()

    return True


# using title to find existed product and update prodict informationr
def update_product(title, new_title, description, price):
    '''
    Update Product info
      Parameters:
        id (integer):           product id
        title (string):         product name
        description (string):   product description
        price (integer):        product price
      Returns:
        Boolean value, true for successful update otherwise update fails
    '''

    # check if the title of the product is not alphanumeric-only,
    # and space allowed only
    if not(all(c.isalnum() or c.isspace() for c in new_title)):
        return None
    # check if prefix or suffix has space
    if ((len(new_title) != 0) and
        (new_title[0] == ' ') or
            (new_title[-1] == ' ')):
        return None
    # check if the title has more than 80 characters
    if len(new_title) > 80:
        return None
    # check if the length of description is less than 20 characters
    # or more than 2000 characters
    if (len(description) < 20) | (len(description) > 2000):
        return None
    # check if the length of description is less than the length of title
    if len(description) < len(new_title):
        return None
    # check if the price is less than 10 or more than 10000
    if (price < 10) | (price > 10000):
        return None

    # search for product that has the same title and overwrites them
    product = Product.query.filter_by(title=title).first()
    # express last modified date in format of dd/mm/yy
    product.last_modified_date = datetime.today().strftime('%Y-%m-%d')
    product.title = new_title
    product.description = description
    # determine wheather new price is incremental than previous one
    if (price < product.price):
        return None
    else:
        product.price = price
    db.session.commit()

    return product
