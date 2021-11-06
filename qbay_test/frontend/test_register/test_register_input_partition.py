import re
import subprocess
from pathlib import Path

# get expected input/output file
current_folder = Path(__file__).parent


# read expected in/out
# email, password and user name all meet the requirement
expected_in1 = open(current_folder.joinpath(
    'input_partition1.in'))
# user name does not meet the requirement
# it's less than 2 character
expected_in2 = open(current_folder.joinpath(
    'input_partition2.in'))
# email does not follow RFC 5322 policy
expected_in3 = open(current_folder.joinpath(
    'input_partition3.in'))
# password does not meet the requirement
# it's less than 6 character length
expected_in4 = open(current_folder.joinpath(
    'input_partition4.in'))
# user name does not meet the requirement
# it's empty
expected_in5 = open(current_folder.joinpath(
    'input_partition5.in'))
# user name does not meet the requirement
# it contains numbers
expected_in6 = open(current_folder.joinpath(
    'input_partition6.in'))
# emails does not meet the requirement
# because they have to be unique
expected_in7 = open(current_folder.joinpath(
    'input_partition7.in'))
# read expected outputs
expected_succeeded_out = open(current_folder.joinpath(
    'test_register_succeeded.out')).read()
expected_failed_out = open(current_folder.joinpath(
    'test_register_failed.out')).read()

print(expected_succeeded_out)
print(expected_failed_out)


def test_register_input_partition():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # testing input partition case 1
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in1,
        capture_output=True,
    ).stdout.decode()
    # remove all whitespace
    convert = re.sub(r'[\x00-\x1f]+', '', output)
    print('outputs', convert)
    assert convert.strip() == expected_succeeded_out.strip()

    # testing input partition case 2
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in2,
        capture_output=True,
    ).stdout.decode()
    # remove all whitespace
    convert = re.sub(r'[\x00-\x1f]+', '', output)
    print('outputs', convert)
    assert convert.strip() == expected_failed_out.strip()

    # testing input partition case 3
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in3,
        capture_output=True,
    ).stdout.decode()
    # remove all whitespace
    convert = re.sub(r'[\x00-\x1f]+', '', output)
    print('Program outputs', convert)
    assert convert.strip() == expected_failed_out.strip()

    # testing input partition case 4
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in4,
        capture_output=True,
    ).stdout.decode()
    # remove all whitespace
    convert = re.sub(r'[\x00-\x1f]+', '', output)
    print('outputs', convert)
    assert convert.strip() == expected_failed_out.strip()

    # testing input partition case 5
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in5,
        capture_output=True,
    ).stdout.decode()
    # remove all whitespace
    convert = re.sub(r'[\x00-\x1f]+', '', output)
    print('outputs', convert)
    assert convert.strip() == expected_failed_out.strip()

    # testing input partition case 6
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in6,
        capture_output=True,
    ).stdout.decode()
    # remove all whitespace
    convert = re.sub(r'[\x00-\x1f]+', '', output)
    print('outputs', convert)
    assert convert.strip() == expected_failed_out.strip()

    # testing input partition case 7
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in7,
        capture_output=True,
    ).stdout.decode()
    # remove all whitespace
    convert = re.sub(r'[\x00-\x1f]+', '', output)
    print('outputs', convert)
    assert convert.strip() == expected_failed_out.strip()
