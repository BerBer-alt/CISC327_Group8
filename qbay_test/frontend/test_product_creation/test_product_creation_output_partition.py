from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent


# get expected in for output partition 1
expected_in_output_partition1 = open(current_folder.joinpath(
    'test_product_creation_output_partition1.in'))
# get expected in for output partition 2
expected_in_output_partition2 = open(current_folder.joinpath(
    'test_product_creation_output_partition2.in'))
# get expected out for succeed case
expected_out_succeed = open(current_folder.joinpath(
    'test_product_creation_succeed.out')).read()
# get expected out for failed case
expected_out_failed = open(current_folder.joinpath(
    'test_product_creation_failed.out')).read()


def test_product_creation_output_partition():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # test for output partition 1
    output1 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_output_partition1,
        capture_output=True,
    ).stdout.decode()
    # judge the output 1
    print('outputs', output1)
    assert output1.strip() == expected_out_succeed.strip()

    # test for output partition 2
    output2 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_output_partition2,
        capture_output=True,
    ).stdout.decode()
    # judge the output 2
    print('outputs', output2)
    assert output2.strip() == expected_out_failed.strip()
