from os import popen
from pathlib import Path
import subprocess
import re

# get expected input/output file
current_folder = Path(__file__).parent

# read expected in/out
expected_in_R1 = open(current_folder.joinpath(
    'test_update_profile_IP_R1.in'))
expected_in_R2 = open(current_folder.joinpath(
    'test_update_profile_IP_R2.in'))
expected_in_R3 = open(current_folder.joinpath(
    'test_update_profile_IP_R3.in'))
expected_in_R4 = open(current_folder.joinpath(
    'test_update_profile_IP_R4.in'))
expected_out_R1 = open(current_folder.joinpath(
    'test_update_profile_IP_R1.out')).read()
expected_out_R2 = open(current_folder.joinpath(
    'test_update_profile_IP_R2.out')).read()
expected_out_R3 = open(current_folder.joinpath(
    'test_update_profile_IP_R3.out')).read()
expected_out_R4 = open(current_folder.joinpath(
    'test_update_profile_IP_R4.out')).read()


def test_update_profile_R1():
    """
        R1: user is able to update its username, address and postal code
    """
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_R1,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_R1.strip()


def test_update_profile_R2():
    """
        R2: wrong user name will lead the update fail and
        return to previous page
    """
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_R2,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_R2.strip()


def test_update_profile_R3():
    """
        R3: invaild address will lead the update fail and
        return to previous page
    """
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_R3,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_R3.strip()


def test_update_profile_R4():
    """
        R3: invaild postalcode will lead the update fail and
        return to previous page
    """
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_R4,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    print('@@@@@@@@@@@@@@@@@@@@@@@\n', output)
    assert con.strip() == expected_out_R4.strip()
