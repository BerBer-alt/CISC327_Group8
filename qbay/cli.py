from qbay.models import login, register, create_product, update_profile, \
    update_product


# The login part
def login_page():
    '''
    User login page
      Parameters: Null
      Returns: Null
    '''
    # Read the values of email and password
    email = input('Please input email: ')
    password = input('Please input password:')
    # Check the correctness of email and password
    return login(email, password)


# The register part
def register_page():
    '''
    Registration page
      Parameters: Null
      Returns: Null
    '''
    # Read the values of name, email, password and confirming password
    name = input('Please input user name: ')
    email = input('Please input email: ')
    password = input('Please input password: ')
    password_twice = input('Please input the password again: ')
    # Compare password with confirming password
    if password != password_twice:
        print('password entered not the same')
    # Register a new user
    elif register(name, email, password):
        print('registration succeeded')
    # Unsuccessful registration
    else:
        print('registration failed.')


# The update_profile part
def profile_update_page(email):
    '''
    Update profile page
      Parameters: identification email
      Returns: Null
    '''
    # Read values of name, shipping_address and postal_code
    name = input("Please change user's name: ")
    shipping_address = input("Please change shipping address: ")
    postal_code = input("Please Change postal code: ")
    # Update the profile
    if update_profile(email, name, shipping_address, postal_code):
        print("Profile Updated Successfully!")
    # Update unsuccessfully
    else:
        print("Profile Update Failed...")


# The create_product part
def product_creation_page():
    '''
    Create product page
      Parameters: Null
      Returns: Null
    '''
    # Read values of title, description, price, last modified date
    # and owner email
    title = input("please input title: ")
    description = input("please input description: ")
    price = int(input("please input price: "))
    last_mod_date = input("please input last modified date")
    owner_email = input("please input owner's email: ")
    # Create a new product
    res = create_product(title, description, price, last_mod_date, owner_email)
    # Create unsuccessfully
    if res is False:
        print("Product Creation failed.")
    # Create successfully
    else:
        print("Creation succeed. ")


# The update_product part
def product_update_page():
    '''
    Update product page
      Parameters: Null
      Returns: Null
    '''
    # Read the values of title(use this to confirm the product), new title,
    # description and price
    title = input("please input former product name: ")
    new_tit = input("please input new product title name: ")
    des = input("please input new product description: ")
    price = int(input("please input new price: "))
    # Update the product
    res = update_product(title, new_tit, des, price)
    # Update unsuccessfully
    if res is None:
        print("update failed")
    # Update successfully
    else:
        print("update succeed")
