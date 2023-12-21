#!/usr/bin/env python3
import argparse

def generate_diff(first_file, second_file, format):
    # Здесь будет ваша логика сравнения файлов
    pass

def main():
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

    # Определение позиционных аргументов
    parser.add_argument('first_file', help='first configuration file')
    parser.add_argument('second_file', help='second configuration file')

    # Определение опционального аргумента --format
    parser.add_argument('-f', '--format', help='set format of output')

    # Разбор аргументов командной строки
    args = parser.parse_args()

    # Вызываем функцию для сравнения файлов
    generate_diff(args.first_file, args.second_file, args.format)

if __name__ == '__main__':
    main()
