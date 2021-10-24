from qbay import *
from qbay.cli import login_page, register_page, profile_update_page
from qbay.cli import product_update_page, product_creation_page


# the function of Frontend CLI
def main():
    # use 'while true' to repeat actions of login or register
    while True:
        # Receive the value of action
        selection = input(
            'Welcome. Please type 1 to login. Or type 2 register.')
        selection = selection.strip()
        # The login part
        if selection == '1':
            # login situation
            user = login_page()
            if user:
                # Return the result of login successfully
                print(f'Welcome back {user.username}')
                # Repeat actions of updating profile,
                # creating product and updating product.
                while True:
                    # Select one action
                    selection = input(
                        "Please type 1 to update your profile.\n"
                        "Type 2 to create product.\n"
                        "Type 3 to update product.\n"
                        "Type something else to exit: ")
                    selection = selection.strip()
                    # Update profile part
                    if selection == '1':
                        profile_update_page(user.email)
                    # Create product part
                    elif selection == '2':
                        product_creation_page()
                    # Update product part
                    elif selection == '3':
                        product_update_page()
                    # Log out
                    else:
                        break
            # Login unsuccessfully
            else:
                print('login failed')
        # register situation
        elif selection == '2':
            register_page()
        # press other character to stop the program
        else:
            break


if __name__ == '__main__':
    main()
