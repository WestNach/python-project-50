import pytest
from gendiff.generate_diff import generate_diff


def open_txt(path_to_file):
    with open('path_to_file', 'r') as file:
        data = file.read()
        return data


@pytest.mark.parametrize(
    "file1, file2, expected_data, format",
    [
        ('tests/fixtures/files/file1.json',
         'tests/fixtures/files/file2.json',
         'tests/fixtures/plain/plain_result.txt', "stylish"),
        ('tests/fixtures/files/file1.yaml',
         'tests/fixtures/files/file2.yaml',
         'tests/fixtures/plain/plain_result.txt', "stylish"),
        ('tests/fixtures/files/file1.json',
         'tests/fixtures/files/file2.json',
         'tests/fixtures/plain/plain_result.txt', "plain"),
        ('tests/fixtures/files/file1.yaml',
         'tests/fixtures/files/file2.yaml',
         'tests/fixtures/plain/plain_result.txt', "plain")
    ]
)
def test_gendiff(first_file, second_file, expected_data, format):
    expected_result = open_txt(expected_data)
    assert generate_diff(first_file, second_file, format) == expected_result
