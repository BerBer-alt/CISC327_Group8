from qbay.models import register, login


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