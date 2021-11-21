from qbay.models import register, login, create_product
import pytest
from pathlib import Path
import subprocess
import re

current_folder = Path(__file__).parent
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
fo = open(current_folder.joinpath(
    'Generic_SQLI.txt'))


def test_cp_p1():
    fo = open(current_folder.joinpath(
        'Generic_SQLI.txt'))
    for item in fo:
        try:
            a = create_product('test 1a', item, 100, '2021-10-07',
                               'aa12a@queensu.ca')
            assert type(a) == bool
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
        except:
            pytest.fail("something else")


def test_cp_p2():
    fo = open(current_folder.joinpath(
        'Generic_SQLI.txt'))
    for item in fo:
        try:
            create_product('test 1a', item, 100, '2021-10-07',
                           'aa12a@queensu.ca')
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
        except:
            pytest.fail("something else exception happened")


def test_cp_p3():
    fo = open(current_folder.joinpath(
        'Generic_SQLI.txt'))
    for item in fo:
        try:
            create_product('test 1b', 'This is a description', item,
                           '2021-10-07', 'aa12a@queensu.ca')
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
        except:
            pytest.fail("something else exception happened")


def test_cp_p4():
    fo = open(current_folder.joinpath(
        'Generic_SQLI.txt'))
    for item in fo:
        try:
            create_product('test 1c', 'This is a description', 100, item,
                           'aa12a@queensu.ca')
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
        except:
            pytest.fail("something else exception happened")


def test_cp_p5():
    fo = open(current_folder.joinpath(
        'Generic_SQLI.txt'))
    for item in fo:
        try:
            create_product('test 1d', 'This is a description', 100,
                           '2021-10-07', item)
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
        except:
            pytest.fail("something else exception happened")


print("test completed")
