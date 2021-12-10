from qbay.models import register, login, create_product
from qbay.models import update_profile, update_product
from qbay.models import Placeorder
from datetime import datetime
from typing import Counter


def test_r1_1_user_register():
    '''
        Testing R1-2: A user is uniquely identified by his/her email address.
        R1-7: If the email has been used, the operation failed.
    '''

    assert register('USER011', 'test011@test.com', 'Hello123!!') is True
    assert register('123123', '', 'Hello123!!') is False
    assert register('USER0', 'test1@test.com', '') is False


def test_r1_2_user_register():
    '''
        Testing R1-2: A user is uniquely identified by his/her email address.
        R1-7: If the email has been used, the operation failed.
    '''

    assert register('USER012', 'test012@test.com', 'Hello123!!') is True
    assert register('USER012', 'test012@test.com', 'Hello123!!') is False
    assert register('USER2', 'Abc.example.com', 'Hello123!!') is False


def test_r1_3_user_register():
    '''
        Testing R1-1: Both the email and password cannot be empty.
    '''

    assert register('User01', 'user01@example.com', '') is False
    assert register('User02', '', 'Abc123!') is False
    assert register('User01', 'user01@example.com', 'Abc012.') is True


def test_r1_4_user_register():
    '''
        Testing R1-3: The email has to follow addr-spec defined in RFC 5322
    '''
    assert register('User02',
                    'i_like_underscore@but_its_not_'
                    'allowed_in_this_part.example.com',
                    'Abc012.') is False
    assert register('User02', 'just\"not\"right@example.com',
                    'Abc123!') is False
    assert register('User02', 'A@b@c@example.com', 'Abc123!') is False
    assert register('User02', '\"john..doe\"@example.org', 'Abc012!') is True
    assert register('User03', 'x@example.com', 'Abc012.') is True
    assert register('User04', 'user.name+tag+sorting@example.com',
                    'Abc012.') is True


def test_r1_5_user_register():
    '''
        Testing R1-4: Password has to meet the required complexity:
        minimum length 6, at least one upper case, at least
        one lower case, and at least one special character.
    '''
    assert register('User05', 'user05@hotmail.com', 'Abc0123?..') is True
    assert register('User06', 'user05@hotmail.com', 'Abc0123') is False
    assert register('User06', 'user05@hotmail.com',
                    'abcdefgsadaxz./???!') is False
    assert register('User06', 'user05@hotmail.com',
                    'Ab2.') is False  # too short


def test_r1_6_user_register():
    '''
        Testing R1-5: User name has to be non-empty, alphanumeric-only,
        and space allowed only if it is not as
        the prefix or suffix.
    '''

    assert register('', 'user07@hotmail.com', 'Ab2.asd') is False
    assert register('sdf~!!@??d', 'user07@hotmail.com', 'Ab2.ssda?') is False
    assert register(' dddsa123', 'user07@hotmail.com', 'Ab2.asd') is False
    assert register('dddsa123 ', 'user07@hotmail.com', 'Ab2.asd') is False
    assert register('User07', 'user07@hotmail.com', 'Ab2.asd') is True


def test_r1_7_user_register():
    '''
        Testing R1-6: User name has to be longer than
        2 characters and less than 20 characters.
    '''
    assert register('W', 'user08@hotmail.com', 'Ab2.asd') is False
    assert register('abcasjudhaksdhaosdijhaolsijdlkasjdiajdliasdjalskdjilja',
                    'user08@hotmail.com', 'Ab2.asd') is False
    assert register('User08', 'user08@hotmail.com', 'Ab2.asd') is True


def test_r2_1_login():
    '''
    Testing R2-1: A user can log in using her/his email address
      and the password.
      R2-2: The login function should check if the supplied
        inputs meet the same email/password requirements as above,
         before checking the database.
    (will be tested after the previous test)
    '''
    user = login('user01@example.com', 'Abc012.')
    assert user is not None
    assert user.username == 'User01'

    user = login('user05@hotmail.com', 'Abc0123?..')
    assert user is not None
    assert user.username == 'User05'

    user = login('user08@hotmail.com', 'Ab2.asd')
    assert user is not None
    assert user.username == 'User08'

    user = login('tuser08@hotmail.com', 'ab2.asd')
    assert user is None

    user = login('test012344@test.com', '1234567')
    assert user is None


def test_r3_1_update_user_profile():
    '''
    Testing R3-1: A user is only able to update
    his/her user name, shipping_address, and postal_code.
    '''
    # create a new user
    assert register('USER0', '12345@qq.com', 'Hello123!!') is True
    # field in all correct parameters
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


def test_r4_1_create_product():
    '''
    Testing R4-1: The title of the product has to be alphanumeric-only, and
    space allowed only if it is not as prefix and suffix.
    '''

    assert create_product('test 1', 'This is a description', 100,
                          '2021-10-07', 'aa12a@queensu.ca') is True
    assert create_product(' test 2', 'This is a description', 100,
                          '2021-10-07', 'aa12a@queensu.ca') is False
    assert create_product('test 3 ', 'This is a description', 100,
                          '2021-10-07', 'aa12a@queensu.ca') is False


def test_r4_2_create_product():
    '''
    Testing R4-2: The title of the product is no longer than 80 characters.
    '''

    assert create_product('test 4', 'This is a description', 100,
                          '2021-10-07', 'aa12a@queensu.ca') is True
    assert create_product('test 5 test 5 test 5 test 5 test 5 test 5 test 5'
                          ' test 5 test 5 test 5 test 5 test 5',
                          'This is a description', 100, '2021-10-07',
                          'aa12a@queensu.ca') is False


def test_r4_3_create_product():
    '''
    Testing R4-3: The description of the product can be arbitrary characters,
    with a minimum length of 20 characters and a maximum of 2000 characters.
    '''

    assert create_product('test 6', 'This is a description', 100, '2021-10-07',
                          'aa12a@queensu.ca') is True
    assert create_product('test 7', 'Description', 100, '2021-10-07',
                          'aa12a@queensu.ca') is False
    assert create_product('test 8', '¡Sí, es verdad! Por eso enseño más '
                          'cursos. Oye… ¿qué hora es?', 100, '2021-10-07',
                          'aa12a@queensu.ca') is True
    assert create_product('test 9', 'The work "done" by the force is the '
                          'scalar product of the force vector and the '
                          'displacement vector of the object. We say that the '
                          'force "does work" if it is exerted while the '
                          'object moves (has a isplacement vector) and in '
                          'such a way that the scalar product of the force '
                          'and displacement vectors is non-zero. A force '
                          'that is perpendicular to the displacement vector '
                          'of an object does no work (since the scalar '
                          'product of two perpendicular vectors is zero). '
                          'A force exerted in the same direction as the '
                          'isplacement will do positive work (cos positive), '
                          'and a force in the opposite direction of the '
                          'displacement will do negative work(cos negative). '
                          'As we will see, positive work corresponds to '
                          'increasing the speed of theobject, whereas '
                          'negative work corresponds to decreasing its '
                          'speed. No work corresponds to no change in speed '
                          '(but could corresponds to a change in velocity). '
                          'You may be tempted to ask, "Why work? Why not '
                          'something else? Why that scalar product in '
                          'particular? How could we possibly have thought of '
                          'that?". In general, it seems arbitrary that we '
                          'introduce the quantity "work" and then find that '
                          'it leads to a convenient way of building models. '
                          'However, we did not just pull this quantity out of '
                          'thin air! Many theorists, over many years, tried '
                          'all sorts of quantities and ways to rephrase '
                          'Newton’s Theory that were not helpful. The '
                          'quantities that make it into textbooks are the '
                          'ones that turned out to be useful. You should also '
                          'keep in mind that, just like force, work is a '
                          '"made-up" mathematical tool that is helpful in '
                          'describing the world around us. There is no such '
                          'thing as work or energy; they are just useful '
                          'mathematical tools. Work involves vectors, so we '
                          'can first examine the concept in one dimension, '
                          'before extending this to two and three dimensions. '
                          'We can choose x as the coordinate in one '
                          'dimension, so that all vectors only have an x '
                          'component. We can write a force vector as '
                          '~F = F ˆx, where F is the x component of the '
                          'force (which could be positive or negative). A '
                          'displacement vector can be written as ~d = dˆx, '
                          'where again, d is the x component of the '
                          'displacement, and can be positive or negative. '
                          'In one dimension, work is thus:', 100, '2021-10-07',
                          'aa12a@queensu.ca') is False


def test_r4_4_create_product():
    '''
    Testing R4-4: Description has to be longer than the product's title.
    '''

    assert create_product('test 10', 'This is a description', 100,
                          '2021-10-07', 'aa12a@queensu.ca') is True
    assert create_product('test 11', 'Test', 100, '2021-10-07',
                          'aa12a@queensu.ca') is False


def test_r4_5_create_product():
    '''
    Testing R4-5: Price has to be of range [10, 10000].
    '''

    assert create_product('test 12', 'This is a description', 100,
                          '2021-10-07', 'aa12a@queensu.ca') is True
    assert create_product('test 13', 'This is a description', 5, '2021-10-07',
                          'aa12a@queensu.ca') is False
    assert create_product('test 14', 'This is a description', 10005,
                          '2021-10-07', 'aa12a@queensu.ca') is False


def test_r4_6_create_product():
    '''
    Testing R4-6: last_modified_date must be after 2021-01-02
    and before 2025-01-02.
    '''

    assert create_product('test 15', 'This is a description', 100,
                          '2021-10-07', 'aa12a@queensu.ca') is True
    assert create_product('test 16', 'This is a description', 100,
                          '2020-10-07', 'aa12a@queensu.ca') is False
    assert create_product('test 17', 'This is a description', 100,
                          '2026-10-07', 'aa12a@queensu.ca') is False


def test_r4_7_create_product():
    '''
    Testing R4-7: owner_email cannot be empty. The owner of the corresponding
    product must exist in the database.
    '''

    assert create_product('test 18', 'This is a description', 100,
                          '2021-10-07', 'aa12a@queensu.ca') is True
    assert create_product('test 19', 'This is a description', 100,
                          '2021-10-07', '') is False
    assert create_product('test 20', 'This is a description', 100,
                          '2021-10-07', 'bb12b@queensu.ca') is True


def test_r4_8_create_product():
    '''
    Testing R4-8: A user cannot create products that have the same title.
    '''

    assert create_product('test 21', 'This is a description', 100,
                          '2021-10-07', 'aa12a@queensu.ca') is True
    assert create_product('test 21', 'This is a description', 100,
                          '2021-10-07', 'aa12a@queensu.ca') is False
    assert create_product('test 18', 'This is a description', 100,
                          '2021-10-07', 'aa12a@queensu.ca') is False


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


def test_r6_r1_Placeorder():
    '''
    R6-1: A user can place an oder on the products.
    '''
    assert Placeorder('user01@example.com', '1') is True


def test_r6_r2_Placeorder():
    '''
    R6-1: A user cannot place an order for his/her products.
    '''
    create_product('candy', 'This is a description', 200,
                   '2021-12-04', 'user05@hotmail.com')
    assert Placeorder('user05@hotmail.com', '12') is False
    assert Placeorder('user05@hotmail.com', '12') is False


def test_r6_r3_Placeorder():
    '''
    R6-1: A user cannot place an order that costs more than his/her balance.
    '''
    assert Placeorder('user07@hotmail.com', '12') is False

