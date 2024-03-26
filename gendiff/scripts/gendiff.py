#!/usr/bin/env python3
from gendiff import generate_diff
from gendiff.parser import parse


def main():
    args = parse()
    diff = generate_diff(args.path1, args.path2, args.format)
    print(diff)


if __name__ == '__main__':
    main()
