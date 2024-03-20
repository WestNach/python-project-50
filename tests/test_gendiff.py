import pytest
from gendiff import generate_diff


def open_txt(path_to_file):
    try:
        with open(path_to_file, 'r') as result:
            data = result.read()
            return data
    except FileNotFoundError as err:
        print(f"File not found: {err}")
        return ""


@pytest.mark.parametrize(
    "file1, file2, expected_data, format",
    [
        ('tests/fixtures/files/file1.json',
         'tests/fixtures/files/file2.json',
         'tests/fixtures/stylish/stylish_result.txt', "stylish"),
        ('tests/fixtures/files/file1.yaml',
         'tests/fixtures/files/file2.yaml',
         'tests/fixtures/stylish/stylish_result.txt', "stylish"),
        ('tests/fixtures/files/file1.json',
         'tests/fixtures/files/file2.json',
         'tests/fixtures/plain/plain_result.txt', "plain"),
        ('tests/fixtures/files/file1.yaml',
         'tests/fixtures/files/file2.yaml',
         'tests/fixtures/plain/plain_result.txt', "plain"),
        ('tests/fixtures/files/file1.yaml',
         'tests/fixtures/files/file2.yaml',
         'tests/fixtures/json/json.txt', "json"),
        ('tests/fixtures/files/file1.json',
         'tests/fixtures/files/file2.json',
         'tests/fixtures/json/json.txt', "json")
    ]
)
def test_gendiff(file1, file2, expected_data, format):
    expected_result = open_txt(expected_data)
    generated_diff = generate_diff(file1, file2, format)
    assert generated_diff == expected_result
