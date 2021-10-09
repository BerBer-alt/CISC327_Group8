from qbay.models import create_product


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
