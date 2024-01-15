import pytest
from gendiff.generate_diff import generate_diff
from fixtures.Flat import flat_result
from fixtures.Recursive import recursive_result


@pytest.mark.parametrize(
    "file1, file2, expected_result",
    [
        ('tests/fixtures/Flat/flat_file1.json',
         'tests/fixtures/Flat/flat_file2.json',
         flat_result),
        ('tests/fixtures/Flat/flat_file1.yaml',
         'tests/fixtures/Flat/flat_file2.yaml',
         flat_result),
        ('tests/fixtures/Recursive/file1.json',
         'tests/fixtures/Recursive/file2.json',
         recursive_result),
        ('tests/fixtures/Recursive/file1.yaml',
         'tests/fixtures/Recursive/file2.yaml',
         recursive_result)
    ]
)
def test_gendiff(first_file, second_file, expected_result):
    assert generate_diff(first_file, second_file) == expected_result
