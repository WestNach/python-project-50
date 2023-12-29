#!/usr/bin/env python3
import argparse
from gendiff import generate_diff


def main():
    disc = 'Compares two configuration files and shows a difference.'
    hl = 'output format (default: "stylish") '
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(description=disc)

    # Определение позиционных аргументов
    parser.add_argument('first_file', help='first configuration file')
    parser.add_argument('second_file', help='second configuration file')
    parser.add_argument('-V', '--version', help='output the version number')
    parser.add_argument('-f', '--format', help=hl)
    args = parser.parse_args()
    different = generate_diff.generate_diff(args.first_file, args.second_file)
    print(different)


if __name__ == '__main__':
    main()
