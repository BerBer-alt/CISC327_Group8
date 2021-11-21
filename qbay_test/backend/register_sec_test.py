from qbay.models import register, login, create_product
import pytest
from pathlib import Path
import subprocess
import re

current_folder = Path(__file__).parent
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
fo = expected_in_R1 = open(current_folder.joinpath(
    'Generic_SQLI.txt'))


def test_reg_p1():
    n = 0
    for i in fo:
        try:
            a = register(i, str(n) + 'test123sec@test.com', 'Password123!')
            assert type(a) == bool
            n += 1
        except:
            pytest.fail(
                "++++++++++++++++++++++++++++++\nfirst argument sec breached")


def test_reg_p2():
    n = 0
    for i in fo:
        try:
            register("UserS" + str(n), i, 'Password123!')
            n += 1
        except:
            pytest.fail(
                "++++++++++++++++++++++++++++++\nsecond argument sec breached")


def test_reg_p3():
    n = 0
    for i in fo:
        try:
            register("UserS" + n, n + 'test123sec@test.com', i)
            n += 1
        except:
            pytest.fail(
                "++++++++++++++++++++++++++++++\nthird argument sec breached")

def test_p3_create_product():
    '''
        Testing third parameter in the create product function.
    '''

    for item in fo:
        try:
            create_product('test 1b', 'This is a description', item,'2021-10-07', 'aa12a@queensu.ca')
        except BaseException as exc:
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
    except ZeroDivisionError as exc:
        pytest.fail(exc, pytrace=True)

print("test completed")
