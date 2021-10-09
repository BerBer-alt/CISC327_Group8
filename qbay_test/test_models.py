from qbay.models import register, login


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
