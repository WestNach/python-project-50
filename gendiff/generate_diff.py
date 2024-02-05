from gendiff.parser import open_file
from gendiff.format.formatting import format_diff


def get_unique_sorted_keys_list(dict1, dict2):
    unique_keys = set(dict1.keys() | dict2.keys())
    keys_list = list(unique_keys)
    keys_list.sort()

    return keys_list


def get_addition_diff(key, value):
    return {
        'change': 'added',
        'value': value
    }


def get_deletion_diff(key, value):
    return {
        'change': 'deleted',
        'value': value
    }


def get_update_diff(key, old_value, new_value):
    return {
        'change': 'updated',
        'old_value': old_value,
        'new_value': new_value
    }


def get_node_diff(key, data1, data2):
    return {
        'change': 'node',
        'children': get_diff(data1, data2)
    }


def get_diff(data1, data2):
    keys = get_unique_sorted_keys_list(data1, data2)
    diff = {}
    for key in keys:
        if key not in data2:
            diff[key] = get_deletion_diff(key, data1[key])
        elif key not in data1:
            diff[key] = get_addition_diff(key, data2[key])
        elif key in data1 and key in data2:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                diff[key] = get_node_diff(key, data1[key], data2[key])
            elif data1[key] != data2[key]:
                diff[key] = get_update_diff(key, data1[key], data2[key])
            elif data1[key] == data2[key]:
                diff[key] = {
                    'change': 'unchanged',
                    'value': data1[key]
                }
    return diff


def generate_diff(first_file, second_file, format='stylish'):
    file1 = open_file(first_file)
    file2 = open_file(second_file)
    diff = get_diff(file1, file2)
    result_differance = format_diff(diff, format)
    return result_differance
