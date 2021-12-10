from qbay.models import Placeorder
from pathlib import Path
import pytest


path = Path(__file__).parent.joinpath('Generic_SQLI.txt')


def test_p1_placeOrder():
    '''
        Testing first parameter in the register function
    '''

    try:
        with open(path) as openfileobject:
            for line in openfileobject:
                Placeorder(line.strip(), 1)
    except NameError as exc:
        pytest.fail(exc, pytrace=True)


def test_p2_placeOrder():
    '''
        Testing second parameter in the register function
    '''

    try:
        with open(path) as openfileobject:
            for line in openfileobject:
                Placeorder("test011@test.com", line.strip())
    except TypeError as exc:
        pytest.fail(exc, pytrace=True)

