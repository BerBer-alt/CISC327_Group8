from qbay import *
from qbay.cli import login_page, register_page, profile_update_page, product_update_page, product_creation_page


def main():
    while True:
        selection = input(
            'Welcome. Please type 1 to login. Or type 2 register.')
        selection = selection.strip()
        if selection == '1':
            user = login_page()
            if user:
                print(f'welcome {user.username}')
                while True:
                    selection = input(
                        "Please type 1 to update your profile."
                        "Type 2 to create product."
                        "Type 3 to update product."
                        "type something else to exit.")
                    selection = selection.strip()
                    if selection == '1':
                        profile_update = profile_update_page()
                    elif selection == '2':
                        product_creation_page()
                    elif selection == '3':
                        product_update_page()
                    else:
                        break
            else:
                print('login failed')
        elif selection == '2':
            register_page()
        else:
            break


if __name__ == '__main__':
    main()
