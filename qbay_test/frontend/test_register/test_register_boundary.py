import re
import subprocess
from pathlib import Path

# get expected input/output file
current_folder = Path(__file__).parent


# read expected in/out
# email, password and user name all meet the requirement
expected_in1 = open(current_folder.joinpath(
    'boundary1.in'))
# email address is very complex but meets
# RFC 5322 requirement
expected_in2 = open(current_folder.joinpath(
    'boundary2.in'))
# password meets the edge of the requirement
# only 6 character length, 1 upper case
# 1 lower case 1 special character
expected_in3 = open(current_folder.joinpath(
    'boundary3.in'))
# user name meets the requirement
# it has 3 characters. more than 2
expected_in4 = open(current_folder.joinpath(
    'boundary4.in'))
# user name meets the requirement
# it has 19 characters. less than 20
expected_in5 = open(current_folder.joinpath(
    'boundary5.in'))
# read expected outputs
expected_succeeded_out = open(current_folder.joinpath(
    'test_register_succeeded.out')).read()
expected_failed_out = open(current_folder.joinpath(
    'test_register_failed.out')).read()

print(expected_succeeded_out)
print(expected_failed_out)


def test_register_boundary():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # testing boundary case 1
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in1,
        capture_output=True,
    ).stdout.decode()
    # remove all whitespace
    convert = re.sub(r'[\x00-\x1f]+', '', output)
    print('outputs', convert)
    assert convert.strip() == expected_succeeded_out.strip()

    # testing boundary case 2
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in2,
        capture_output=True,
    ).stdout.decode()
    # remove all whitespace
    convert = re.sub(r'[\x00-\x1f]+', '', output)
    print('outputs', convert)
    assert convert.strip() == expected_succeeded_out.strip()

    # testing boundary case 3
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in3,
        capture_output=True,
    ).stdout.decode()
    # remove all whitespace
    convert = re.sub(r'[\x00-\x1f]+', '', output)
    print('outputs', convert)
    assert convert.strip() == expected_succeeded_out.strip()

    # testing boundary case 4
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in4,
        capture_output=True,
    ).stdout.decode()
    # remove all whitespace
    convert = re.sub(r'[\x00-\x1f]+', '', output)
    print('outputs', convert)
    assert convert.strip() == expected_succeeded_out.strip()

    # testing boundary case 5
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in5,
        capture_output=True,
    ).stdout.decode()
    # remove all whitespace
    convert = re.sub(r'[\x00-\x1f]+', '', output)
    print('outputs', convert)
    assert convert.strip() == expected_succeeded_out.strip()
