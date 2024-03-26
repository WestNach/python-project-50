import yaml
import json
import os
from gendiff.formats.formatting import format_diff
from gendiff.diff import get_diff


# Open and parse file based on extension
def open_file(path):
    _, extension = (os.path.splitext(path))
    if extension == ".json":
        with open(path) as f:
            file = json.load(f)
    elif extension == ".yaml" or extension == ".yml":
        with open(path) as f:
            file = yaml.load(f, Loader=yaml.FullLoader)
    else:
        raise ValueError(f'Unsupported file format: {extension}')
    return file


def generate_diff(first_file, second_file, output_format="stylish"):
    file1 = open_file(first_file)
    file2 = open_file(second_file)
    difference = get_diff(file1, file2)
    result_differance = format_diff(difference, output_format)
    return result_differance
