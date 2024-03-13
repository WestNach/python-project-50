import yaml
import json
import os


def open_file(file_path):
    name_of_file, file_extension = (os.path.splitext(file_path))
    if file_extension == ".json":
        with open(file_path) as f:
            file = json.load(f)
    elif file_extension == ".yaml" or file_extension == ".yml":
        with open(file_path) as f:
            file = yaml.load(f, Loader=yaml.FullLoader)
    else:
        raise ValueError(f'Unsupported file format: {file_extension}')
    return file
