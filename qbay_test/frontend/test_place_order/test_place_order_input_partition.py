from os import popen
from pathlib import Path
import subprocess
import re

# get expected input/output file
current_folder = Path(__file__).parent


# get expected in for input partition 1
expected_in_input_partition1 = open(current_folder.joinpath(
    'test_place_order_input_partition1.in'))
# get expected in for input partition 2
expected_in_input_partition2 = open(current_folder.joinpath(
    'test_place_order_input_partition2.in'))
# get expected in for input partition 3
expected_in_input_partition3 = open(current_folder.joinpath(
    'test_place_order_input_partition3.in'))
# get expected in for input partition 4
expected_in_input_partition4 = open(current_folder.joinpath(
    'test_place_order_input_partition4.in'))
# get expected in for input partition 5
expected_in_input_partition5 = open(current_folder.joinpath(
    'test_place_order_input_partition5.in'))
# get expected out for input partition 1
expected_out_input_partition1 = open(current_folder.joinpath(
    'test_place_order_input_partition1.out')).read()
# get expected out for input partition 2
expected_out_input_partition2 = open(current_folder.joinpath(
    'test_place_order_input_partition2.out')).read()
# get expected out for input partition 3
expected_out_input_partition3 = open(current_folder.joinpath(
    'test_place_order_input_partition3.out')).read()
# get expected out for input partition 4
expected_out_input_partition4 = open(current_folder.joinpath(
    'test_place_order_input_partition4.out')).read()
# get expected out for input partition 5
expected_out_input_partition5 = open(current_folder.joinpath(
    'test_place_order_input_partition5.out')).read()


def test_place_order_input_partition():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # test for input partition 1
    output1 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_input_partition1,
        capture_output=True,
    ).stdout.decode()
    # judge the output 1
    con = re.sub(r'[\x00-\x1f]', '', output1)
    assert con.strip() == expected_out_input_partition1.strip()

    # test for input partition 2
    output2 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_input_partition2,
        capture_output=True,
    ).stdout.decode()
    # judge the output 2
    con2 = re.sub(r'[\x00-\x1f]', '', output2)
    assert con2.strip() == expected_out_input_partition2.strip()

    # test for input partition 3
    output3 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_input_partition3,
        capture_output=True,
    ).stdout.decode()
    # judge the output 3
    con = re.sub(r'[\x00-\x1f]', '', output3)
    assert con.strip() == expected_out_input_partition3.strip()

    # test for input partition 4
    output4 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_input_partition4,
        capture_output=True,
    ).stdout.decode()
    # judge the output 4
    con = re.sub(r'[\x00-\x1f]', '', output4)
    assert con.strip() == expected_out_input_partition4.strip()

    # test for input partition 5
    output5 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_input_partition5,
        capture_output=True,
    ).stdout.decode()
    # judge the output 5
    con = re.sub(r'[\x00-\x1f]', '', output5)
    assert con.strip() == expected_out_input_partition5.strip()
