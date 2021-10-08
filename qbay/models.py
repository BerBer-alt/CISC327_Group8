from qbay import app
from flask_sqlalchemy import SQLAlchemy
import re

'''
This file defines data models and related business logics
'''


# this function check if the Email address inputed fits the format or not
def check_Email(Input_str: str):
    if Input_str == "":
        return False
    regex = r"(^[a-zA-Z0-9_.+-/!#$%&'*/=?^_`{|}~\" ]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
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
    if domain.find("..") != -1 or domain.find(" ") != -1:
        return False

    return True


# this function check the string that input fits the requirnment or not
def check_Password(Input_password: str):
    # not implemented yet
    return True


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


db = SQLAlchemy(app)


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


# create all tables
db.create_all()


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
        shipping_address="",
        postal_code="",
        balance=100)
    # add it to the current database session
    db.session.add(user)
    # actually save the user object
    db.session.commit()

    return True


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
