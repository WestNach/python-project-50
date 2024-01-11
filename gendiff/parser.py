import yaml
import json
import argparse
import os


def parser_data(first_file, second_file):
    disc = "Compares two configuration files and shows a difference."
    hl = 'output format (default: "stylish") '

    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(description=disc)

    # Определение позиционных аргументов
    parser.add_argument("first_file", help="first configuration file")
    parser.add_argument("second_file", help="second configuration file")
    parser.add_argument("-V", "--version", help="output the version number")
    parser.add_argument("-f", "--format", help=hl)
    args = parser.parse_args()
    return args


def open_file(file_path):
    name_of_file = os.path.splitext(file_path)[1]
    if name_of_file == ".json":
        file = json.load(open(file_path))
    elif name_of_file == ".yaml" or name_of_file == ".yml":
        file = yaml.load(open(file_path), Loader=yaml.FullLoader)
    return file
