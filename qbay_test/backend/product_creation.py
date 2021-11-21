import pytest
from qbay.models import register, create_product
print("-----------------------------------------------")

def test_p1_create_product():
    '''
        Testing first parameter in the create product function.
    '''

    try:
        with open('Generic_SQLI.txt') as test_list:
            for item in test_list:
                create_product(item, 'This is a description', 100,
                               '2021-10-07', 'aa12a@queensu.ca')
    except:
        pytest.fail(exc, pytrace=True)


def test_p2_create_product():
    '''
        Testing second parameter in the create product function.
    '''
    try:
        with open('Generic_SQLI.txt') as test_list:
            for item in test_list:
                create_product('test 1a', item, 100, '2021-10-07',
                               'aa12a@queensu.ca')
    except:
        pytest.fail(exc, pytrace=True)


def test_p3_create_product():
    '''
        Testing third parameter in the create product function.
    '''
    try:
        with open('Generic_SQLI.txt') as test_list:
            for item in test_list:
                create_product('test 1b', 'This is a description', item,
                               '2021-10-07', 'aa12a@queensu.ca')
    except:
        pytest.fail(exc, pytrace=True)


def test_p4_create_product():
    '''
        Testing fourth parameter in the create product function.
    '''
    try:
        with open('Generic_SQLI.txt') as test_list:
            for item in test_list:
                create_product('test 1c', 'This is a description', 100, item,
                               'aa12a@queensu.ca')
    except:
        pytest.fail(exc, pytrace=True)


def test_p5_create_product():
    '''
        Testing fifth parameter in the create product function.
    '''
    try:
        with open('Generic_SQLI.txt') as test_list:
            for item in test_list:
                create_product('test 1d', 'This is a description', 100,
                               '2021-10-07', item)
    except:
        pytest.fail(exc, pytrace=True)
