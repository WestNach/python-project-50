from gendiff.parser import open_file
from gendiff.formats.formatting import format_diff
from .diff import get_diff


def get_file_data(file_path):
    file_data = open_file(file_path)
    return file_data


def generate_diff(first_file, second_file, output_format="stylish"):
    file1 = get_file_data(first_file)
    file2 = get_file_data(second_file)
    difference = get_diff(file1, file2)
    result_differance = format_diff(difference, output_format)
    return result_differance
