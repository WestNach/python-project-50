#!/usr/bin/env python3
import argparse
from gendiff.parser import open_file
from gendiff.formats.formatting import format_diff
from gendiff.diff import get_diff


def get_file_data(file_path):
    file_data = open_file(file_path)
    return file_data


def generate_diff(first_file, second_file, output_format="stylish"):
    file1 = get_file_data(first_file)
    file2 = get_file_data(second_file)
    difference = get_diff(file1, file2)
    result_differance = format_diff(difference, output_format)
    return result_differance


def main():
    parser = argparse.ArgumentParser(
        description='Generate difference between two files')
    parser.add_argument('path1', help='path to the first file')
    parser.add_argument('path2', help='path to the second file')
    parser.add_argument('-f', '--format', choices=['plain', 'stylish', 'json'],
                        default='stylish',
                        help='output format (default: stylish)')
    args = parser.parse_args()

    diff = generate_diff(args.path1, args.path2, args.format)
    print(diff)


if __name__ == '__main__':
    main()
