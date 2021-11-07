from os import popen
from pathlib import Path
import subprocess
import re

# get expected input/output file
current_folder = Path(__file__).parent

# --------- Input partitioning testing
# read expected in/out
# all the input meet the requirement
expected_in_R1 = open(current_folder.joinpath(
    'test_update_profile_IP_R1.in'))
# user name does not meet the requirement
# update should fail
expected_in_R2 = open(current_folder.joinpath(
    'test_update_profile_IP_R2.in'))
# street address is empty
expected_in_R3 = open(current_folder.joinpath(
    'test_update_profile_IP_R3.in'))
# postal code does not meet the requirement
expected_in_R4 = open(current_folder.joinpath(
    'test_update_profile_IP_R4.in'))
# read expected outputs
expected_out_R1 = open(current_folder.joinpath(
    'test_update_profile_IP_R1.out')).read()
expected_out_R2 = open(current_folder.joinpath(
    'test_update_profile_IP_R2.out')).read()
expected_out_R3 = open(current_folder.joinpath(
    'test_update_profile_IP_R3.out')).read()
expected_out_R4 = open(current_folder.joinpath(
    'test_update_profile_IP_R4.out')).read()


def test_update_profile():
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

    """
        R2: wrong user name will lead the update fail and return to previous page
    """
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_R2,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_R2.strip()

    """
        R3: invalid address will lead the update fail and return to previous page
    """
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_R3,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_R3.strip()

    """
        R3: invalid postalcodes will lead the update fail and return to previous page
    """
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_R4,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_R4.strip()
