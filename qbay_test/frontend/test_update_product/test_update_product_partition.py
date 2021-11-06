from os import popen
from pathlib import Path
import subprocess
import re

# get expected input/output file
current_folder = Path(__file__).parent

# Input Partition Testing
# no change to the product title
expected_in_partition1 = open(current_folder.joinpath(
    'partition1.in'))
# change product title to integer
expected_in_partition2 = open(current_folder.joinpath(
    'partition2.in'))
# product title more than 80 characters
expected_in_partition3 = open(current_folder.joinpath(
    'partition3.in'))
# prefix or suffix has space
expected_in_partition4 = open(current_folder.joinpath(
    'partition4.in'))
# product description less than 20
expected_in_partition5 = open(current_folder.joinpath(
    'partition5.in'))
# length of description is less than length of title
expected_in_partition6 = open(current_folder.joinpath(
    'partition6.in'))
# price of product is less than 10 or more than 10000
expected_in_partition7 = open(current_folder.joinpath(
    'partition7.in'))

# success output
expected_out_partition_succeed = open(current_folder.joinpath(
    'partition_succeed.out')).read()
# failure output
expected_out_partition_failed = open(current_folder.joinpath(
    'partition_failed.out')).read()


def test_update_product_partition():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # partition1
    output = subprocess.run(
        ['python3', '-m', 'qbay'],
        stdin=expected_in_partition1,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_partition_succeed.strip()

    # partition2
    output = subprocess.run(
        ['python3', '-m', 'qbay'],
        stdin=expected_in_partition2,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_partition_succeed.strip()

    # partition3
    output = subprocess.run(
        ['python3', '-m', 'qbay'],
        stdin=expected_in_partition3,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_partition_failed.strip()

    # partition4
    output = subprocess.run(
        ['python3', '-m', 'qbay'],
        stdin=expected_in_partition4,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_partition_failed.strip()

    # partition5
    output = subprocess.run(
        ['python3', '-m', 'qbay'],
        stdin=expected_in_partition5,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_partition_failed.strip()

    # partition6
    output = subprocess.run(
        ['python3', '-m', 'qbay'],
        stdin=expected_in_partition6,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_partition_failed.strip()

    # partition7
    output = subprocess.run(
        ['python3', '-m', 'qbay'],
        stdin=expected_in_partition7,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_partition_failed.strip()
