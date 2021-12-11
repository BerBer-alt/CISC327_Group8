from qbay import app
from flask_sqlalchemy import SQLAlchemy
import re
from datetime import datetime
import difflib

db = SQLAlchemy(app)


# the class for user objects
class User(db.Model):
    # email attribute with 120 maximum string length, can't be empty
    email = db.Column(
        db.String(120), unique=True, nullable=False,
        primary_key=True)
    # username attribute with 80 maximum string length, can't be empty
    username = db.Column(
        db.String(80), nullable=False)
    # password attribute with 120 maximum string length, can't be empty
    password = db.Column(
        db.String(120), nullable=False)
    # shipping address attribute with 120 maximum string length, can be empty
    shipping_address = db.Column(
        db.String(120), unique=False, nullable=True,
        primary_key=False)
    # postal code attribute with 120 maximum string length, can be empty
    postal_code = db.Column(
        db.String(120), unique=False, nullable=True,
        primary_key=False)
    # balance attribute as in integer, can be empty
    balance = db.Column(
        db.Integer,
        unique=False,
        nullable=True,
        primary_key=False)

    def __repr__(self):
        return '<User %r>' % self.username


# the class for transaction objects, unique=True/False decides if
# the attribute is unique or not. nullable =True/false decides if the
# attribute can be empty or not.
class Transaction(db.Model):
    # id attribute is the primary key as in integer
    id = db.Column(db.Integer, primary_key=True)
    # user email attribute with 120 maximum string length
    user_email = db.Column(db.String(120), unique=True, nullable=False)
    # product id attribute with 80 maximum string length
    product_id = db.Column(db.String(80), unique=True, nullable=False)
    # price attribute as in integer
    price = db.Column(db.Integer, unique=False, nullable=False)
    # date attribute with 120 maximum string length
    date = db.Column(db.String(10), unique=False, nullable=False)

    def __repr__(self):
        return "<Transaction %r>" % self.id


# the class for product objects, unique=True/False decides if
# # the attribute is unique or not. nullable =True/false decides if the
# # attribute can be empty or not.
class Product(db.Model):
    # id attribute is the primary key as in integer
    id = db.Column(db.Integer, primary_key=True)
    # title id attribute with 80 maximum string length
    title = db.Column(db.String(80), unique=True, nullable=True)
    # description attribute with 2000 maximum string length
    description = db.Column(db.String(2000), unique=False, nullable=False)
    # price attribute as in integer
    price = db.Column(db.Integer, unique=False, nullable=False)
    # last modified date attribute with 10 maximum string length
    last_modified_date = db.Column(db.String(10), unique=False, nullable=False)
    # owner_email attribute with 120 maximum string length
    owner_email = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return "<Product %r>" % self.id


# the class for review objects, unique=True/False decides if
# # # the attribute is unique or not. nullable =True/false decides if the
# # # attribute can be empty or not.
class Review(db.Model):
    # id attribute is the primary key as in integer
    id = db.Column(db.Integer, primary_key=True)
    # user_email attribute with 120 maximum string length
    user_email = db.Column(
        db.String(120), unique=True, nullable=False)
    # score attribute as in integer
    score = db.Column(db.Integer, unique=True, nullable=False)
    # review text attribute with 500 maximum string length
    review_text = db.Column(db.String(500), unique=False, nullable=False)

    def __repr__(self):
        return '<Review %r>' % self.review_id


# create all tables
db.create_all()


# this function check if the Email address inputed fits the format or not
def check_Email(Input_str: str):
    # email address can't be empty
    if Input_str == "":
        return False
    # email validation regular expression as in RFC 5322 Policy
    regex = r"(^[a-zA-Z0-9_.+-/!#$%&'*/=?^_`{|}~\" ]" \
            r"+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    # if the email address does not match the regex return false
    if re.search(regex, Input_str) is None:
        return False
    # start and end of the local can't be dot
    local = Input_str[0:Input_str.index("@")]
    if local[0] == "." or local[-1] == ".":
        return False
    # A local part is either a Dot-string or a Quoted-string,
    # not a combination.
    # quoted strings must be dot separated or the only element
    # making up the local-part.spaces, quotes, and backslashes may
    # only exist when within quoted strings and preceded by a backslash
    # even if escaped (preceded by a backslash), spaces, quotes,
    # and backslashes must still be contained by quotes
    if local.find("\"") != -1:
        fir_q = local.find("\"")
        sec_q = local.find("\"", fir_q + 1)
        if sec_q == -1:
            return False
        local = local[0:fir_q] + local[sec_q + 1:]
        if local.find(".") == -1 and fir_q != 0 and sec_q != len(Input_str):
            return False
    if local.find("..") != -1 or local.find(" ") != -1:
        return False

    return True


# this function check the input password string fits the requirement or not
def check_Password(Input_password: str):
    # the minimum length of input password string should be 6
    if Input_password.__len__() < 6:
        return False
    Flag_upper = False
    Flag_lower = False
    Flag_Spec = False
    # Password has to meet the required complexity: minimum length 6,
    # at least one upper case, at least one lower case,
    # and at least one special character.
    for i in Input_password:
        if i.isupper():
            Flag_upper = True
        elif i.islower():
            Flag_lower = True
        elif i in "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~":
            Flag_Spec = True
    return Flag_Spec and Flag_lower and Flag_upper


# this function check the input string fits the user requirnment or not
def check_Username(Input_Username: str):
    # User name has to be longer than 2 characters and
    # less than 20 characters.
    if Input_Username.__len__() <= 2 or Input_Username.__len__() > 20:
        return False
    # User name has to be non-empty, alphanumeric-only,
    # and space allowed only if it is not as the prefix or suffix.
    if Input_Username[0] == " " or Input_Username[-1] == " ":
        return False
    for i in Input_Username:
        if not i.isalnum():
            return False
    return True


# function used to register as an user with name, email address and password
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
    # check user name, email address, and password requirements
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
        # free $100 dollar signup bonus
        balance=100)
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
    email = email.strip()
    password = password.strip()
    # check email and password requirements
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
    if not isinstance(price, int):
        return False
    # check if the title of the product is not alphanumeric-only,
    # and space allowed only
    if not (all(c.isalnum() or c.isspace() for c in title)):
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

    # shipping address should not be empty or contain no special characters
    if (not (shipping_address) or
            (shipping_address.isalnum() is False)):
        return False
    # Canadian zip code configuration
    if not ((len(re.findall(
            r'[A-Z]{1}[0-9]{1}[A-Z]{1}\s*[0-9]{1}[A-Z]{1}[0-9]{1}',
            postal_code.upper()))) == 1):
        return False
    # user name should not empty and not space at prefix or suffix
    if (not (name) or len(name) >= 20 or len(name) <= 2 or
            name[0] == " " or
            name[-1] == " " or
            not (all(i.isalnum() or i.isspace() for i in name))):
        return False

    # overwrite each attribute of the product
    user = User.query.filter_by(email=email).first()
    user.username = name
    user.postal_code = postal_code
    user.shipping_address = shipping_address
    db.session.commit()

    return True


# using title to find existed product and update product information
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
    # check if prefix or suffix has space
    if ((len(new_title) != 0) and
            (new_title[0] == ' ') or
            (new_title[-1] == ' ')):
        return None

    title = title.strip()
    new_title = new_title.strip()

    # check if the title of the product is not alphanumeric-only,
    # and space allowed only
    if not (all(c.isalnum() or c.isspace() for c in new_title)):
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
    # determine whether new price is incremental than previous one
    if price < product.price:
        return None
    else:
        product.price = price
    db.session.commit()

    return product


# Use user's email and product id to place an order.
def Placeorder(buyer_email, product_id):
    '''
    Place an order.
      Parameters:
        buyer_email (string):   buyer's email
        product_id  (string):   product id
      Returns:
        Boolean value, true for successful order otherwise order fails
    '''
    user_b = User.query.filter_by(email=buyer_email).first()
    product = Product.query.filter_by(id=product_id).first()
    try:
        # if buyer's email is same as owner's email, buyer cannot buy
        # this product.
        if buyer_email == product.owner_email:
            return False
        # if buyer does not have enough money, buyer cannot buy this
        # product.
        if user_b.balance < product.price:
            return False

        # place an order and put this transaction into the database.
        user_b.balance -= product.price
        product.owner_email = buyer_email
        date_n = datetime.today().strftime('%Y-%m-%d')
        new_transaction = Transaction(
            id=db.session.query(Transaction).count() + 1,
            user_email=buyer_email,
            product_id=product_id,
            price=product.price,
            date=date_n)
        db.session.add(new_transaction)
        db.session.commit()
        return True
    except BaseException:
        return False
