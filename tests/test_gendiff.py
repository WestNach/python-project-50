import pytest
from gendiff.generate_diff import generate_diff
import os


def normalize_file_name(filepath):
    return filepath.replace('/', os.sep).replace('\\', os.sep)


def read_file(filepath):  # load file
    with open(normalize_file_name(filepath)) as file:
        return file.read()


@pytest.mark.parametrize(
    "file1, file2, expected_result",
    [
        (('tests/fixtures/files/file1.json'),
         ('tests/fixtures/files/file2.json'),
         read_file('tests/fixtures/flat_json_result.txt')),
    ]
)
def test_gendiff(first_file, second_file, expected_result):
    assert generate_diff(first_file, second_file) == expected_result
