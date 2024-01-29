#!/usr/bin/env python3
from gendiff.generate_diff import generate_diff
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Generate difference between two files')
    parser.add_argument('filepath1', help='path to the first file')
    parser.add_argument('filepath2', help='path to the second file')
    parser.add_argument('-f', '--format', choices=['plain', 'stylish', 'json'],
                        default='stylish',
                        help='output format (default: stylish)')
    args = parser.parse_args()

    diff = generate_diff(args.filepath1, args.filepath2, args.fromat)
    print(diff)


if __name__ == '__main__':
    main()
