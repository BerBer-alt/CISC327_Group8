from os import popen
from pathlib import Path
import subprocess
import re

# get expected input/output file
current_folder = Path(__file__).parent

# read expected in/out
# case 1 profile updated succeeded
# all the input should meet the requirements
expected_in_R1 = open(current_folder.joinpath(
    'test_update_profile_OP_R1.in'))
# case 2 profile updated failed
# input should not meet the requirements
expected_in_R2 = open(current_folder.joinpath(
    'test_update_profile_OP_R2.in'))
# output when the profile update succeeded
expected_out_R1 = open(current_folder.joinpath(
    'test_update_profile_OP_R1.out')).read()
# output when the profile update failed
expected_out_R2 = open(current_folder.joinpath(
    'test_update_profile_OP_R2.out')).read()


def test_update_profile_R1():
    """
        testing output partitioning case 1
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
        testing output partitioning case 2
    """
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_R2,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_R2.strip()
