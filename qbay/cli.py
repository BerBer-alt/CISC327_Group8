<<<<<<< HEAD
from qbay.models import login, register


def login_page():
    email = input('Please input email')
    password = input('Please input password:')
    return login(email, password)


def regsiter_page():
    email = input('Please input email:')
    password = input('Please input password:')
    password_twice = input('Please input the password again:')
    if password != password_twice:
        print('password entered not the same')
    elif register('default name', email, password):
        print('registration succceeded')
    else:
        print('regisration failed.')

def profile_update_page():
    '''
    Update profile page
      Parameters:
        
      Returns:
        
    '''
=======
from qbay.models import login, register, create_product, update_profile, \
    update_product


def login_page():
    email = input('Please input email: ')
    password = input('Please input password:')
    return login(email, password)


def register_page():
    name = input('Please input user name: ')
    email = input('Please input email: ')
    password = input('Please input password: ')
    password_twice = input('Please input the password again: ')
    if password != password_twice:
        print('password entered not the same')
    elif register(name, email, password):
        print('registration succeeded')
    else:
        print('registration failed.')


def profile_update_page():
    email = input("please input email: ")
    name = input("please input user's name: ")
    shipping_address = input("please input shipping address: ")
    postal_code = input("please input postal code: ")
    if update_profile(email, name, shipping_address, postal_code):
        print("profile updated")
    else:
        print("profile update failed. ")


def product_creation_page():
    title = input("please input title: ")
    description = input("please input description: ")
    price = int(input("please input price: "))
    last_mod_date = input("please input last modified date")
    owner_email = input("please input owner's email: ")
    res = create_product(title, description, price, last_mod_date, owner_email)
    if res is False:
        print("Product Creation failed.")
    else:
        print("Creation succeed. ")


def product_update_page():
    title = input("please input former product name: ")
    new_tit = input("please input new product title name: ")
    des = input("please input new product description: ")
    price = int(input("please input new price: "))
    res = update_product(title, new_tit, des, price)
    if res is None:
        print("update failed")
    else:
        print("update succeed")
>>>>>>> 87976097484665130d7741551d282f114ffade07
