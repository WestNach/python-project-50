import pytest
from gendiff.generate_diff import generate_diff
from fixtures.Flat import flat_result
from fixtures.stylish import stylish_result
from fixtures.plain import plain_result


@pytest.mark.parametrize(
    "file1, file2, expected_result, format",
    [
        ('tests/fixtures/Flat/flat_file1.json',
         'tests/fixtures/Flat/flat_file2.json',
         flat_result),
        ('tests/fixtures/Flat/flat_file1.yaml',
         'tests/fixtures/Flat/flat_file2.yaml',
         flat_result),
        ('tests/fixtures/stylish/file1.json',
         'tests/fixtures/stylish/file2.json',
         stylish_result, "stylish"),
        ('tests/fixtures/stylish/file1.yaml',
         'tests/fixtures/stylish/file2.yaml',
         stylish_result, "stylish")
        ('tests/fixtures/stylish/file1.json',
         'tests/fixtures/stylish/file2.json',
         plain_result, "plain"),
        ('tests/fixtures/stylish/file1.yaml',
         'tests/fixtures/stylish/file2.yaml',
         plain_result, "plain")
    ]
)
def test_gendiff(first_file, second_file, expected_result, format):
    assert generate_diff(first_file, second_file, format) == expected_result
