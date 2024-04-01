import argparse
import yaml
import json


def open_and_parse_data(path, extension):
    if extension == ".json":
        with open(path) as f:
            file = json.load(f)
    elif extension == ".yaml" or extension == ".yml":
        with open(path) as f:
            file = yaml.load(f, Loader=yaml.FullLoader)
    else:
        raise ValueError(f'Unsupported file format: {extension}')
    return file


# Function to parse command line arguments
def parse():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(
        # Provide a description of the script
        description='Generate difference between two files')

    # Add arguments to the parser
    parser.add_argument('path1', help='path to the data1')
    parser.add_argument('path2', help='path to the data2')

    # Add optional argument with format choices
    parser.add_argument('-f', '--format', choices=['plain', 'stylish', 'json'],
                        # Set the default format as 'stylish'
                        default='stylish',
                        # Provide a help message for the --format argument
                        help='output format (default: stylish)')

    # Parse the arguments and return them as an object
    args = parser.parse_args()
    return args
