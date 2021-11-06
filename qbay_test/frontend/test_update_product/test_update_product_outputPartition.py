from os import popen
from pathlib import Path
import subprocess
import re

# get expected input/output file
current_folder = Path(__file__).parent

# Output Partition Testing
# if output is update succeed, then product title could contain
# space and alphanumeric, description is between 20 and 2000
# price is between 10 and 10000.
expected_in_outputPartition1 = open(current_folder.joinpath(
    'outputPartition1.in'))
# if output is update failed, then product title could be all space,
# description is less than 20 and price is more than 10000.
expected_in_outputPartition2 = open(current_folder.joinpath(
    'outputPartition2.in'))

# success output
expected_out_partition_succeed = open(current_folder.joinpath(
    'outputPartition_succeed.out')).read()
# failure output
expected_out_partition_failed = open(current_folder.joinpath(
    'outputPartition_failed.out')).read()


def test_update_product_OutputPartition():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # Output Partition1
    output = subprocess.run(
        ['python3', '-m', 'qbay'],
        stdin=expected_in_outputPartition1,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_partition_succeed.strip()

    # Output Partition2
    output = subprocess.run(
        ['python3', '-m', 'qbay'],
        stdin=expected_in_outputPartition2,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_partition_failed.strip()
