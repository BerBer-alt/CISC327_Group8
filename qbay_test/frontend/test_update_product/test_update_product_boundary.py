from os import popen
from pathlib import Path
import subprocess
import re
from qbay.models import register, create_product

# get expected input/output file
current_folder = Path(__file__).parent

# Input Boundary Testing
# product title is alphanumeric-only, including space
expected_in_boundary1 = open(current_folder.joinpath(
    'boundary1.in'))
# print("#####"+expected_in_boundary1.read()+"####")
# product title's prefix or suffix do not have space
expected_in_boundary2 = open(current_folder.joinpath(
    'boundary2.in'))
# product title is less than 80 characters
expected_in_boundary3 = open(current_folder.joinpath(
    'boundary3.in'))
# product description is between 20 to 2000 characters
expected_in_boundary4 = open(current_folder.joinpath(
    'boundary4.in'))
# length of description is greater than the length of title
expected_in_boundary5 = open(current_folder.joinpath(
    'boundary5.in'))
# product price is between 10 and 10000
expected_in_boundary6 = open(current_folder.joinpath(
    'boundary6.in'))

# success output
expected_out_boundary_succeed = open(current_folder.joinpath(
    'boundary_succeed.out')).read()
# failure output
expected_out_boundary_failed = open(current_folder.joinpath(
    'boundary_failed.out')).read()

# initialise user login and create product
#register('User08', 'user08@hotmail.com', 'Ab2.asd')
# create_product(
#         'apple',
#         'This is a description',
#         10, '2021-10-07',
#         'aa12a@queensu.ca')

def test_update_product_boundary():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # boundary1
    output = subprocess.run(
        ['python3', '-m', 'qbay'],
        stdin=expected_in_boundary1,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_boundary_succeed.strip()

    # boundary2
    output = subprocess.run(
        ['python3', '-m', 'qbay'],
        stdin=expected_in_boundary2,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_boundary_succeed.strip()

    # boundary3
    output = subprocess.run(
        ['python3', '-m', 'qbay'],
        stdin=expected_in_boundary3,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_boundary_succeed.strip()

    # boundary4
    output = subprocess.run(
        ['python3', '-m', 'qbay'],
        stdin=expected_in_boundary4,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_boundary_succeed.strip()

    # boundary5
    output = subprocess.run(
        ['python3', '-m', 'qbay'],
        stdin=expected_in_boundary5,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_boundary_succeed.strip()

    # boundary6
    output = subprocess.run(
        ['python3', '-m', 'qbay'],
        stdin=expected_in_boundary6,
        capture_output=True,
    ).stdout.decode()
    con = re.sub(r'[\x00-\x1f]', '', output)
    assert con.strip() == expected_out_boundary_succeed.strip()
