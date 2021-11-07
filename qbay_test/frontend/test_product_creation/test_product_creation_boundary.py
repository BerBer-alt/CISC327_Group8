from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent


# get expected in for boundary 1
expected_in_boundary1 = open(current_folder.joinpath(
    'test_product_creation_boundary1.in'))
# get expected in for boundary 2
expected_in_boundary2 = open(current_folder.joinpath(
    'test_product_creation_boundary2.in'))
# get expected in for boundary 3
expected_in_boundary3 = open(current_folder.joinpath(
    'test_product_creation_boundary3.in'))
# get expected in for boundary 4
expected_in_boundary4 = open(current_folder.joinpath(
    'test_product_creation_boundary4.in'))
# get expected in for boundary 5
expected_in_boundary5 = open(current_folder.joinpath(
    'test_product_creation_boundary5.in'))
# get expected out for succeed case
expected_out_succeed = open(current_folder.joinpath(
    'test_product_creation_succeed.out')).read()
# get expected out for failed case
expected_out_failed = open(current_folder.joinpath(
    'test_product_creation_failed.out')).read()


def test_product_creation_boundary():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # test for boundary 1
    output1 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_boundary1,
        capture_output=True,
    ).stdout.decode()
    # judge the output 1
    print('outputs', output1)
    assert output1.strip() == expected_out_failed.strip()

    # test for boundary 2
    output2 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_boundary2,
        capture_output=True,
    ).stdout.decode()
    # judge the output 2
    print('outputs', output2)
    assert output2.strip() == expected_out_succeed.strip()

    # test for boundary 3
    output3 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_boundary3,
        capture_output=True,
    ).stdout.decode()
    # judge the output 3
    print('outputs', output3)
    assert output3.strip() == expected_out_failed.strip()

    # test for boundary 4
    output4 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_boundary4,
        capture_output=True,
    ).stdout.decode()
    # judge the output 4
    print('outputs', output4)
    assert output4.strip() == expected_out_failed.strip()

    # test for boundary 5
    output5 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_boundary5,
        capture_output=True,
    ).stdout.decode()
    # judge the output 5
    print('outputs', output5)
    assert output5.strip() == expected_out_failed.strip()
