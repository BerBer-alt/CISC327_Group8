from os import popen
from pathlib import Path
import subprocess
import re

# get expected input/output file
current_folder = Path(__file__).parent

# --------- boundary testing
# read expected in/out
# all the input meet the requirement
expected_in_R1 = open(current_folder.joinpath(
    'test_update_profile_boundary_R1.in'))
# user name does not meet the requirement
# update should fail
expected_in_R2 = open(current_folder.joinpath(
    'test_update_profile_boundary_R2.in'))
# Shipping address is non-empty, alphanumeric-only
# and contains no special characters
expected_in_R3 = open(current_folder.joinpath(
    'test_update_profile_boundary_R3.in'))
# postal code is weird but still meets the requirement
expected_in_R4 = open(current_folder.joinpath(
    'test_update_profile_boundary_R4.in'))
# read expected outputs
expected_out = open(current_folder.joinpath(
    'test_update_profile_boundary.out')).read()


def test_update_profile_boundary():

    # boundary testing case 1
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_R1,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out.strip()

    # boundary testing case 2
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_R2,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out.strip()

    # boundary testing case 3
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_R3,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out.strip()

    # boundary testing case 4
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_R4,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out.strip()
