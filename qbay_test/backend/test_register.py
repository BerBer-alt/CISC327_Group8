from qbay.models import register, create_product
from pathlib import Path
import pytest

def test_p1_register():
    '''
        Testing first parameter in the register function
    '''
    
    try:
        with open(Path(__file__).parent.joinpath('Generic_SQLI.txt')) as openfileobject:
            for line in openfileobject:
                # with pytest.raises(eLib.NameError):
                register(line.strip(), 'test123@test.com', 'Hello123!!')
    except NameError as exc:
        pytest.fail(exc, pytrace=True)


def test_p2_register():
    '''
        Testing second parameter in the register function
    '''
    
    try:
        with open(Path(__file__).parent.joinpath('Generic_SQLI.txt')) as openfileobject:
            for line in openfileobject:
                # with pytest.raises(eLib.NameError):
                register('test123', line.strip(), 'Hello123!!')
    except TypeError as exc:
        pytest.fail(exc, pytrace=True)


def test_p3_register():
    '''
        Testing second parameter in the register function
    '''
    
    try:
        with open(Path(__file__).parent.joinpath('Generic_SQLI.txt')) as openfileobject:
            for line in openfileobject:
                # with pytest.raises(eLib.NameError):
                register('test123', 'test123@test.com', line.strip())
    except ValueError as exc:
        pytest.fail(exc, pytrace=True)
