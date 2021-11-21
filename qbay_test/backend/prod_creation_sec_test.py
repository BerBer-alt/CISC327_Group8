from qbay.models import register, login, create_product
import pytest
from pathlib import Path

# open the file Generic_SQLI.txt for fuzzy test
current_folder = Path(__file__).parent
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
fo = open(current_folder.joinpath(
    'Generic_SQLI.txt'))


# fuzzy test 1 for create product function
def test_cp_p1():
    '''
        Testing first parameter in the create product function.
    '''
    # open file
    fo = open(current_folder.joinpath(
        'Generic_SQLI.txt'))
    # go through every line in the file
    for item in fo:
        try:
            # try to create a product
            test = create_product(item, 'This is a description', 100,
                                  '2021-10-07', 'aa12a@queensu.ca')
            assert isinstance(test, bool)
        # judge different errors
        except RuntimeError as exc:
            pytest.fail(exc)
        except NameError as exc:
            pytest.fail(exc)
        except ValueError as exc:
            pytest.fail(exc)
        except ZeroDivisionError as exc:
            print("ZeroDivisionError happened")
            pytest.fail(exc)
        except NotImplementedError as exc:
            pytest.fail(exc)
        except TypeError as exc:
            pytest.fail(exc)
        except UserWarning as exc:
            pytest.fail(exc)
        except BaseException:
            pytest.fail("something else")


# fuzzy test 2 for create product function
def test_cp_p2():
    '''
        Testing second parameter in the create product function.
    '''
    # open file
    fo = open(current_folder.joinpath(
        'Generic_SQLI.txt'))
    # go through every line in the file
    for item in fo:
        try:
            # try to create a product
            create_product('test 1a', item, 100, '2021-10-07',
                           'aa12a@queensu.ca')
        # judge different errors
        except RuntimeError as exc:
            pytest.fail(exc)
        except NameError as exc:
            pytest.fail(exc)
        except ValueError as exc:
            pytest.fail(exc)
        except ZeroDivisionError as exc:
            print("ZeroDivisionError happened")
            pytest.fail(exc)
        except NotImplementedError as exc:
            pytest.fail(exc)
        except TypeError as exc:
            pytest.fail(exc)
        except UserWarning as exc:
            pytest.fail(exc)
        except BaseException:
            pytest.fail("something else exception happened")


# fuzzy test 3 for create product function
def test_cp_p3():
    '''
        Testing third parameter in the create product function.
    '''
    # open file
    fo = open(current_folder.joinpath(
        'Generic_SQLI.txt'))
    # go through every line in the file
    for item in fo:
        try:
            # try to create a product
            create_product('test 1b', 'This is a description', item,
                           '2021-10-07', 'aa12a@queensu.ca')
        # judge different errors
        except RuntimeError as exc:
            pytest.fail(exc)
        except ValueError as exc:
            pytest.fail(exc)
        except ZeroDivisionError as exc:
            print("ZeroDivisionError happened")
            pytest.fail(exc)
        except NotImplementedError as exc:
            pytest.fail(exc)
        except TypeError as exc:
            pytest.fail(exc)
        except UserWarning as exc:
            pytest.fail(exc)
        except BaseException:
            pytest.fail("something else exception happened")


# fuzzy test 4 for create product function
def test_cp_p4():
    '''
        Testing fourth parameter in the create product function.
    '''
    # open file
    fo = open(current_folder.joinpath(
        'Generic_SQLI.txt'))
    # go through every line in the file
    for item in fo:
        try:
            # try to create a product
            create_product('test 1c', 'This is a description', 100, item,
                           'aa12a@queensu.ca')
        # judge different errors
        except RuntimeError as exc:
            pytest.fail(exc)
        except NameError as exc:
            pytest.fail(exc)
        except ValueError as exc:
            pytest.fail(exc)
        except ZeroDivisionError as exc:
            print("ZeroDivisionError happened")
            pytest.fail(exc)
        except NotImplementedError as exc:
            pytest.fail(exc)
        except TypeError as exc:
            pytest.fail(exc)
        except UserWarning as exc:
            pytest.fail(exc)
        except BaseException:
            pytest.fail("something else exception happened")


# fuzzy test 5 for create product function
def test_cp_p5():
    '''
        Testing fifth parameter in the create product function.
    '''
    # open file
    fo = open(current_folder.joinpath(
        'Generic_SQLI.txt'))
    # go through every line in the file
    for item in fo:
        try:
            # try to create a product
            create_product('test 1d', 'This is a description', 100,
                           '2021-10-07', item)
        # judge different errors
        except RuntimeError as exc:
            pytest.fail(exc)
        except NameError as exc:
            pytest.fail(exc)
        except ValueError as exc:
            pytest.fail(exc)
        except ZeroDivisionError as exc:
            print("ZeroDivisionError happened")
            pytest.fail(exc)
        except NotImplementedError as exc:
            pytest.fail(exc)
        except TypeError as exc:
            pytest.fail(exc)
        except UserWarning as exc:
            pytest.fail(exc)
        except BaseException:
            pytest.fail("something else exception happened")


print("test completed")
