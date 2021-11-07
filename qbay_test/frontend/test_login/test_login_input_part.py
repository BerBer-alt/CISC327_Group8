from os import popen
from pathlib import Path
import subprocess
import re

# get expected input/output file
current_folder = Path(__file__).parent

# read expected in/out
expected_in_R1 = open(current_folder.joinpath(
    'test_login_IP_R1.in'))
expected_in_R2 = open(current_folder.joinpath(
    'test_login_IP_R2.in'))
expected_in_R3 = open(current_folder.joinpath(
    'test_login_IP_R3.in'))
expected_out_R1 = open(current_folder.joinpath(
    'test_login_IP_R1.out')).read()
expected_out_R2 = open(current_folder.joinpath(
    'test_login_IP_R2.out')).read()
expected_out_R3 = open(current_folder.joinpath(
    'test_login_IP_R3.out')).read()


def test_login_R1():
    """
        R1: A user can log in using her/his email address and the password.
        The wright input e-mail and password will lead to the right profile
        page
    """
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_R1,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    # print('@@@@@@@@@@@@@@@@@@@@@@@\n', output)
    # print("#######################\n",expected_out)
    assert con.strip() == expected_out_R1.strip()


def test_login_R2():
    """
            R2: A wrong email cannot login the page
            The wrong input e-mail and password will lead to the failure
    """
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_R2,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    # print('22@@@@@@@@@@@@@@@@@@@@@@@\n', output)
    # print("#######################\n",expected_out)
    assert con.strip() == expected_out_R2.strip()


def test_login_R3():
    """
                R3: The login function should check if the supplied inputs meet
                the
                same email/password requirements asabove, before checking the
                database.
                The invalid input e-mail and password will lead to the
                failure
    """
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_R3,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    #  print('33@@@@@@@@@@@@@@@@@@@@@@@\n', output)
    # print("#######################\n",expected_out)
    assert con.strip() == expected_out_R3.strip()
