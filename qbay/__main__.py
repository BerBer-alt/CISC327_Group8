from qbay import *
from qbay.cli import login_page, register_page, profile_update_page
from qbay.cli import product_update_page, product_creation_page


def main():
    while True:
        selection = input(
            'Welcome. Please type 1 to login. Or type 2 register.')
        selection = selection.strip()
        if selection == '1':
            # login situation
            user = login_page()
            if user:
                print(f'Welcome back {user.username}')
                while True:
                    selection = input(
                        "Please type 1 to update your profile.\n"
                        "Type 2 to create product.\n"
                        "Type 3 to update product.\n"
                        "Type something else to exit: ")
                    selection = selection.strip()
                    if selection == '1':
                        profile_update_page(user.email)
                    elif selection == '2':
                        product_creation_page()
                    elif selection == '3':
                        product_update_page()
                    else:
                        break
            else:
                print('login failed')
        elif selection == '2':
            # register situation
            register_page()
        else:
            # press other character to stop the program
            break


if __name__ == '__main__':
    main()
