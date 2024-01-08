import pytest
from gendiff.generate_diff import generate_diff
from fixtures.Flat import flat_result
from fixtures.Recursive import recursive_result
import json
import yaml

@pytest.mark.parametrize(
    "file1, file2, expected_result",
    [
        (json.load(open('tests/fixtures/Flat/flat_file1.json')),
         json.load(open('tests/fixtures/Flat/flat_file2.json')),
         flat_result),
        (yaml.load(open('tests/fixtures/Flat/flat_file1.yaml'), Loader=yaml.FullLoader),
         yaml.load(open('tests/fixtures/Flat/flat_file2.yaml'), Loader=yaml.FullLoader),
         flat_result)
        (json.load(open('tests/fixtures/Recursive/file1.json')),
         json.load(open('tests/fixtures/Recursive/file2.json')),
         recursive_result),
        (yaml.load(open('tests/fixtures/Recursive/file1.yaml'), Loader=yaml.FullLoader),
         yaml.load(open('tests/fixtures/Recursive/file2.yaml'), Loader=yaml.FullLoader),
         recursive_result)
    ]
)
def test_gendiff(first_file, second_file, expected_result: str):
    assert generate_diff(first_file, second_file) == expected_result
