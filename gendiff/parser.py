import yaml
import json
import argparse
import os


def parser_data(first_file, second_file):
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

    file1 = os.path.splitext(first_file)[1]
    if file1 == ".json":
        first_file = json.load(open(args.first_file))
        second_file = json.load(open(args.second_file))
    elif file1 == ".yaml" or file1 == ".yml":
        first_file = yaml.load(open(args.first_file), Loader=yaml.FullLoader)
        second_file = yaml.load(open(args.second_file), Loader=yaml.FullLoader)
    return first_file, second_file
