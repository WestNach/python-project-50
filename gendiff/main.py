
from gendiff.formats.formatting import format_diff
from gendiff.diff import get_diff
import os
from gendiff.parser import open_and_parse_data


def generate_diff(path1, path2, output_format="stylish"):
    _, extension1 = (os.path.splitext(path1))
    _, extension2 = (os.path.splitext(path2))
    file1 = open_and_parse_data(path1, extension1)
    file2 = open_and_parse_data(path2, extension2)
    difference = get_diff(file1, file2)
    result_differance = format_diff(difference, output_format)
    return result_differance
