#!/usr/bin/env python3
from gendiff import generate_diff
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Generate difference between two files')
    parser.add_argument('path1', help='path to the first file')
    parser.add_argument('path2', help='path to the second file')
    parser.add_argument('-f', '--format', choices=['plain', 'stylish', 'json'],
                        default='stylish',
                        help='output format (default: stylish)')
    args = parser.parse_args()

    diff = generate_diff.generate_diff(args.path1, args.path2, args.format)
    print(diff)


if __name__ == '__main__':
    main()
