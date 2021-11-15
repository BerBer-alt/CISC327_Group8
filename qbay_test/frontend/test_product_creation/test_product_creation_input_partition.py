from os import popen
from pathlib import Path
import subprocess
import re

# get expected input/output file
current_folder = Path(__file__).parent


# get expected in for input partition 1
expected_in_input_partition1 = open(current_folder.joinpath(
    'test_product_creation_input_partition1.in'))
# get expected in for input partition 2
expected_in_input_partition2 = open(current_folder.joinpath(
    'test_product_creation_input_partition2.in'))
# get expected in for input partition 3
expected_in_input_partition3 = open(current_folder.joinpath(
    'test_product_creation_input_partition3.in'))
# get expected in for input partition 4
expected_in_input_partition4 = open(current_folder.joinpath(
    'test_product_creation_input_partition4.in'))
# get expected in for input partition 5
expected_in_input_partition5 = open(current_folder.joinpath(
    'test_product_creation_input_partition5.in'))
# get expected in for input partition 6
expected_in_input_partition6 = open(current_folder.joinpath(
    'test_product_creation_input_partition6.in'))
# get expected in for input partition 7
expected_in_input_partition7 = open(current_folder.joinpath(
    'test_product_creation_input_partition7.in'))
# get expected out for succeed case
expected_out_succeed = open(current_folder.joinpath(
    'test_product_creation_succeed.out')).read()
# get expected out for failed case
expected_out_failed = open(current_folder.joinpath(
    'test_product_creation_failed.out')).read()


def test_product_creation_input_partition():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # test for input partition 1
    output1 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_input_partition1,
        capture_output=True,
    ).stdout.decode()
    # judge the output 1
    print('outputs', output1)
    con = re.sub(r'[\x00-\x1f]', '', output1)
    assert con.strip() == expected_out_succeed.strip()

    # test for input partition 2
    output2 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_input_partition2,
        capture_output=True,
    ).stdout.decode()
    # judge the output 2
    print('outputs', output2)
    con = re.sub(r'[\x00-\x1f]', '', output2)
    assert con.strip() == expected_out_succeed.strip()

    # test for input partition 3
    output3 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_input_partition3,
        capture_output=True,
    ).stdout.decode()
    # judge the output 3
    print('outputs', output3)
    con = re.sub(r'[\x00-\x1f]', '', output3)
    assert con.strip() == expected_out_failed.strip()

    # test for input partition 4
    output4 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_input_partition4,
        capture_output=True,
    ).stdout.decode()
    # judge the output 4
    con = re.sub(r'[\x00-\x1f]', '', output4)
    assert con.strip() == expected_out_failed.strip()

    # test for input partition 5
    output5 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_input_partition5,
        capture_output=True,
    ).stdout.decode()
    # judge the output 5
    print('outputs', output5)
    con = re.sub(r'[\x00-\x1f]', '', output5)
    assert con.strip() == expected_out_failed.strip()

    # test for input partition 6
    output6 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_input_partition6,
        capture_output=True,
    ).stdout.decode()
    # judge the output 6
    print('outputs', output6)
    con = re.sub(r'[\x00-\x1f]', '', output6)
    assert con.strip() == expected_out_succeed.strip()

    # test for input partition 7
    output7 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_input_partition7,
        capture_output=True,
    ).stdout.decode()
    # judge the output 7
    print('outputs', output7)
    con = re.sub(r'[\x00-\x1f]', '', output7)
    assert con.strip() == expected_out_failed.strip()
