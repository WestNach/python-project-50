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
        (('tests/fixtures/Flat/file1.json'),
         ('tests/fixtures/Flat/file2.json'),
         read_file('tests/fixtures/Flat/flat_result.txt')),
        (('tests/fixtures/Flat/file1.yaml'),
         ('tests/fixtures/Flat/file2.yaml'),
         read_file('tests/fixtures/Flat/flat_result.txt'))
        (('tests/fixtures/files/nested_file1.json'),
         ('tests/fixtures/files/nested_file2.json'),
         read_file('tests/fixtures/Recursive/recursive_result.txt')),
        (('tests/fixtures/files/nested_file1.yaml'),
         ('tests/fixtures/files/nested_file2.yaml'),
         read_file('tests/fixtures/Recursive/recursive_result.txt'))
    ]
)
def test_gendiff(first_file, second_file, expected_result: str):
    assert generate_diff(first_file, second_file) == expected_result
