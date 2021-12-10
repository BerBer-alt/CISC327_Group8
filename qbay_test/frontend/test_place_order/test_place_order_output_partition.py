from os import popen
from pathlib import Path
import subprocess
import re

# get expected input/output file
current_folder = Path(__file__).parent


# get expected in for output partition 1
expected_in_output_partition1 = open(current_folder.joinpath(
    'test_place_order_output_partition1.in'))
# get expected in for output partition 2
expected_in_output_partition2 = open(current_folder.joinpath(
    'test_place_order_output_partition2.in'))
# get expected in for output partition 3
expected_in_output_partition3 = open(current_folder.joinpath(
    'test_place_order_output_partition3.in'))
# get expected in for output partition 4
expected_in_output_partition4 = open(current_folder.joinpath(
    'test_place_order_output_partition4.in'))
# get expected out for output partition 1
expected_out_output_partition1 = open(current_folder.joinpath(
    'test_place_order_output_partition1.out')).read()
# get expected out for output partition 2
expected_out_output_partition2 = open(current_folder.joinpath(
    'test_place_order_output_partition2.out')).read()
# get expected out for output partition 3
expected_out_output_partition3 = open(current_folder.joinpath(
    'test_place_order_output_partition3.out')).read()
# get expected out for output partition 4
expected_out_output_partition4 = open(current_folder.joinpath(
    'test_place_order_output_partition4.out')).read()


def test_place_order_output_partition():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # test for output partition 1
    output1 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_output_partition1,
        capture_output=True,
    ).stdout.decode()
    # judge the output 1
    con = re.sub(r'[\x00-\x1f]', '', output1)
    assert con.strip() == expected_out_output_partition1.strip()

    # test for output partition 2
    output2 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_output_partition2,
        capture_output=True,
    ).stdout.decode()
    # judge the output 2
    con = re.sub(r'[\x00-\x1f]', '', output2)
    assert con.strip() == expected_out_output_partition2.strip()

    # test for output partition 3
    output3 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_output_partition3,
        capture_output=True,
    ).stdout.decode()
    # judge the output 3
    con = re.sub(r'[\x00-\x1f]', '', output3)
    assert con.strip() == expected_out_output_partition3.strip()

    # test for output partition 4
    output4 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_output_partition4,
        capture_output=True,
    ).stdout.decode()
    # judge the output 4
    con = re.sub(r'[\x00-\x1f]', '', output4)
    assert con.strip() == expected_out_output_partition4.strip()
