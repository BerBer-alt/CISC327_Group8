import re
import subprocess
from pathlib import Path

# get expected input/output file
current_folder = Path(__file__).parent


# read expected in/out
# case 1 when output succeeded
# input should meet all the requirements
expected_in1 = open(current_folder.joinpath(
    'output_partition1.in'))
# case 2 when output failed
# input should be wrong
expected_in2 = open(current_folder.joinpath(
    'output_partition2.in'))

# read expected succeeded outputs
expected_succeeded_out = open(current_folder.joinpath(
    'test_register_succeeded.out')).read()
# read expected failed outputs
expected_failed_out = open(current_folder.joinpath(
    'test_register_failed.out')).read()

print(expected_succeeded_out)
print(expected_failed_out)


def test_register_input_partition():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # case 1 success output
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in1,
        capture_output=True,
    ).stdout.decode()
    # remove all whitespace
    convert = re.sub(r'[\x00-\x1f]+', '', output)
    print('outputs', convert)
    assert convert.strip() == expected_succeeded_out.strip()

    # case 2 failed output
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in2,
        capture_output=True,
    ).stdout.decode()
    # remove all whitespace
    convert = re.sub(r'[\x00-\x1f]+', '', output)
    print('outputs', convert)
    assert convert.strip() == expected_failed_out.strip()
