from qbay.models import register, login
from typing import Counter
from datetime import datetime
from qbay.models import Product, User, update_product, update_profile
from qbay.models import create_product

def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''

    assert register('USER0', 'test0@test.com', 'Hello123!!') is True
    assert register('USER1', 'test1@test.com', 'Hello123!!') is True
    assert register('USER2', 'test2@test.com', 'Hello123!!') is True
    assert register('USER3', 'test3@test.com', 'Hello123!!') is True
    assert register('USER4', 'test4@test.com', 'Hello123!!') is True
    assert register('u1', 'test0@test.com', '123456') is False


def test_r2_1_login():
    '''
    Testing R2-1: A user can log in using her/his email address
      and the password.
    (will be tested after the previous test, so we already have u0,
      u1 in database)
    '''

    user = login('test0@test.com', "Hello123!!")
    assert user is not None
    assert user.username == 'USER0'

    user = login('test1@test.com', "Hello123!!")
    assert user is not None
    assert user.username == 'USER1'

    user = login('test2@test.com', "Hello123!!")
    assert user is not None
    assert user.username == 'USER2'

    user = login('test3@test.com', "Hello123!!")
    assert user is not None
    assert user.username == 'USER3'

    user = login('test4@test.com', "Hello123!!")
    assert user is not None
    assert user.username == 'USER4'

    user = login('test0@test.com', "Hello1asdasdasd?????????")
    assert user is None

    user = login('testXXX@test.com', "Hello123!!")
    assert user is None


def test_r3_1_update_user_profile():
    '''
    Testing R2-1: A user is only able to update
    his/her user name, shipping_address, and postal_code.
    '''
    assert register('USER0', '12345@qq.com', 'Hello123!!') is True
    assert update_profile("12345@qq.com", 'Tom',
                          '123UniversityAve', 'K7L 0Y3') is True


def test_r3_2_update_user_profile():
    '''
    R3-2: Shipping_address should be non-empty,
    alphanumeric-only, and no special characters such as !
    '''
    assert update_profile("12345@qq.com", 'Tom', '', 'K7L 0Y3') is False
    assert update_profile(
                        "12345@qq.com",
                        'Tom',
                        '123! University Ave',
                        'K7L 0Y3') is False


def test_r3_3_update_user_profile():
    '''
    R3-3: Postal code has to be a valid Canadian postal code
    '''
    assert update_profile(
            "12345@qq.com",
            'Tom',
            '123UniversityAve',
            'K7L 0Y3') is True
    assert update_profile(
        "12345@qq.com",
        'Tom',
        '123UniversityAve',
        'K0Y3') is False


def test_r3_4_update_user_profile():
    '''
    R3-4: User name follows the requirements above
    '''
    assert update_profile(
        "12345@qq.com",
        'm',
        '123UniversityAve',
        'K7L 0Y3') is False
    assert update_profile(
        "12345@qq.com",
        'qwertyuiopasdfghjklz',
        '123UniversityAve',
        'K7L 0Y3') is False
    assert update_profile(
        "12345@qq.com",
        '',
        '123 University Ave',
        'K7L 0Y3') is False
    assert update_profile(
        "12345@qq.com",
        ' Tim ',
        '123UniversityAve',
        'K7L 0Y3') is False


def test_r5_1_update_product():
    '''
    R5-1: One can update all attributes of the product,
    except owner_email and last_modified_date
    '''

    product = create_product(
        'apple',
        'This is a description',
        10, '2021-10-07',
        'aa12a@queensu.ca')
    assert update_product(
        "apple",
        "apple",
        "an apple a day keeps doctor away",
        30) is not None


def test_r5_2_update_product():
    '''
    R5-2: Price can be only increased but cannot be decreased
    '''

    assert update_product(
        "apple",
        "apple",
        "good for health good for health",
        29) is None


def test_r5_3_update_product():
    '''
    R5-3: last_modified_date should be updated when the
    update operation is successful
    '''
    product = update_product(
        "apple",
        "apple",
        "good for health good for health",
        1000)
    # check if the last_modified_date is corrected updated after update_product
    assert product.last_modified_date == datetime.today().strftime('%Y-%m-%d')


def test_r5_4_update_product():
    '''
    R5-4: When updating an attribute, one has to make sure
    that it follows the same requirements as above
    '''

    assert update_product(
        "apple",
        "apple",
        "good for health good for health",
        2000) is not None

    assert update_product(
        "apple",
        "apple ",
        "good for health good for health",
        1006) is None
