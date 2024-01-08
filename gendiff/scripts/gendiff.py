#!/usr/bin/env python3
from gendiff import generate_diff
from gendiff import parser


def main():
    first_file, second_file = parser.pareser_data()
    different = generate_diff.generate_diff(first_file, second_file)
    return print(different)


if __name__ == '__main__':
    main()
