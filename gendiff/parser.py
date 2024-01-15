import yaml
import json
import os


def open_file(file_path):
    name_of_file = os.path.splitext(file_path)[1]
    if name_of_file == ".json":
        file = json.load(open(file_path))
    elif name_of_file == ".yaml" or name_of_file == ".yml":
        file = yaml.load(open(file_path), Loader=yaml.FullLoader)
    else:
        raise ValueError(f'Unsupported file format: {name_of_file}')
    return file
