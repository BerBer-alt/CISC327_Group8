from os import popen
from pathlib import Path
import subprocess
import re

# get expected input/output file
current_folder = Path(__file__).parent

# read expected in/out
expected_r1 = open(current_folder.joinpath(
    'test_login_st_reg1.in'))

test_login_st_in1 = open(current_folder.joinpath(
    'test_login_st_1.in'))
test_login_st_in2 = open(current_folder.joinpath(
    'test_login_st_2.in'))
test_login_st_in3 = open(current_folder.joinpath(
    'test_login_st_3.in'))

expected_out_1 = open(current_folder.joinpath(
    'test_login_st_1.out')).read()
expected_out_2 = open(current_folder.joinpath(
    'test_login_st_2.out')).read()
expected_out_3 = open(current_folder.joinpath(
    'test_login_st_3.out')).read()

output = subprocess.run(
    ['python', '-m', 'qbay'],
    stdin=expected_r1,
    capture_output=True,
).stdout.decode()


def test_login_st_1():
    """
        Test the login with random existed account
    """
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=test_login_st_in1,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_1.strip()


def test_login_st_2():
    """
        Test the login with random not existed account
    """
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=test_login_st_in2,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_2.strip()


def test_login_st_3():
    """
        Test the random existed account
    """
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=test_login_st_in3,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_3.strip()
