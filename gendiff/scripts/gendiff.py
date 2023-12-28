#!/usr/bin/env python3
import argparse
from gendiff import generate_diff


def main():
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

    # Определение позиционных аргументов
    parser.add_argument('first_file', help='first configuration file')
    parser.add_argument('second_file', help='second configuration file')
    parser.add_argument('-V', '--version', help='output the version number')
    parser.add_argument('-f', '--format', help='output format (default: "stylish") ')
    args = parser.parse_args()
    diff = generate_diff(args.file_path1, args.file_path2)
    print(diff)

if __name__ == '__main__':
    main()
