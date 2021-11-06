from os import popen
from pathlib import Path
import subprocess
import re

# get expected input/output file
current_folder = Path(__file__).parent

# read expected in/out
expected_r1 = open(current_folder.joinpath(
    'test_login_ro_reg1.in'))
expected_r2 = open(current_folder.joinpath(
    'test_login_ro_reg2.in'))
test_login_ro_in1 = open(current_folder.joinpath(
    'test_login_ro_1.in'))
test_login_ro_in2 = open(current_folder.joinpath(
    'test_login_ro_2.in'))
test_login_ro_in3 = open(current_folder.joinpath(
    'test_login_ro_3.in'))
test_login_ro_in4 = open(current_folder.joinpath(
    'test_login_ro_4.in'))
expected_out_1 = open(current_folder.joinpath(
    'test_login_ro_1.out')).read()
expected_out_2 = open(current_folder.joinpath(
    'test_login_ro_2.out')).read()
expected_out_3 = open(current_folder.joinpath(
    'test_login_ro_3.out')).read()
expected_out_4 = open(current_folder.joinpath(
    'test_login_ro_4.out')).read()

output = subprocess.run(
    ['python', '-m', 'qbay'],
    stdin=expected_r1,
    capture_output=True,
).stdout.decode()

output = subprocess.run(
    ['python', '-m', 'qbay'],
    stdin=expected_r2,
    capture_output=True,
).stdout.decode()


def test_login_ro_1():
    """
        Test the email with length of 120
    """
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=test_login_ro_in1,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_1.strip()


def test_login_ro_2():
    """
        Test the empty email
    """
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=test_login_ro_in2,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_2.strip()


def test_login_ro_3():
    """
        Test the password with length of 120
    """
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=test_login_ro_in3,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    # print('33@@@@@@@@@@@@@@@@@@@@@@@\n', output)
    # print("#######################\n", expected_out_3)
    assert con.strip() == expected_out_3.strip()


def test_login_ro_4():
    """
        Test the empty email
    """
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=test_login_ro_in4,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_4.strip()
