from pathlib import Path
import subprocess
import re

# get expected input/output file
current_folder = Path(__file__).parent


# get expected in for boundary 1
expected_in_boundary1 = open(current_folder.joinpath(
    'test_place_order_boundary1.in'))
# get expected in for boundary 2
expected_in_boundary2 = open(current_folder.joinpath(
    'test_place_order_boundary2.in'))
# get expected in for boundary 3
expected_in_boundary3 = open(current_folder.joinpath(
    'test_place_order_boundary3.in'))
# get expected in for boundary 4
expected_in_boundary4 = open(current_folder.joinpath(
    'test_place_order_boundary4.in'))
# get expected in for boundary 5
expected_in_boundary5 = open(current_folder.joinpath(
    'test_place_order_boundary5.in'))
# get expected out for boundary 1
expected_out_boundary1 = open(current_folder.joinpath(
    'test_place_order_boundary1.out')).read()
# get expected out for boundary 2
expected_out_boundary2 = open(current_folder.joinpath(
    'test_place_order_boundary2.out')).read()
# get expected out for boundary 3
expected_out_boundary3 = open(current_folder.joinpath(
    'test_place_order_boundary3.out')).read()
# get expected out for boundary 4
expected_out_boundary4 = open(current_folder.joinpath(
    'test_place_order_boundary4.out')).read()
# get expected out for boundary 5
expected_out_boundary5 = open(current_folder.joinpath(
    'test_place_order_boundary5.out')).read()


def test_place_order_boundary():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # test for boundary 1
    output1 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_boundary1,
        capture_output=True,
    ).stdout.decode()
    # judge the output 1
    con = re.sub(r'[\x00-\x1f]', '', output1)
    assert con.strip() == expected_out_boundary1.strip()

    # test for boundary 2
    output2 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_boundary2,
        capture_output=True,
    ).stdout.decode()
    # judge the output 2
    con = re.sub(r'[\x00-\x1f]', '', output2)
    assert con.strip() == expected_out_boundary2.strip()

    # test for boundary 3
    output3 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_boundary3,
        capture_output=True,
    ).stdout.decode()
    # judge the output 3
    con = re.sub(r'[\x00-\x1f]', '', output3)
    assert con.strip() == expected_out_boundary3.strip()

    # test for boundary 4
    output4 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_boundary4,
        capture_output=True,
    ).stdout.decode()
    # judge the output 4
    con = re.sub(r'[\x00-\x1f]', '', output4)
    assert con.strip() == expected_out_boundary4.strip()

    # test for boundary 5
    output5 = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_boundary5,
        capture_output=True,
    ).stdout.decode()
    # judge the output 5
    con = re.sub(r'[\x00-\x1f]', '', output5)
    assert con.strip() == expected_out_boundary5.strip()
