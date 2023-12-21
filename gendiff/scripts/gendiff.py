#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='First file')
    parser.add_argument('second_file', help='Second file')
    args = parser.parse_args()

    # Ваш код для выполнения операций с файлами


if __name__ == '__main__':
    main()
