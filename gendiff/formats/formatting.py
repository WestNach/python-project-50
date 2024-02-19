from gendiff.formats import json
from gendiff.formats import plain
from gendiff.formats import stylish


def format_diff(difference, output_format='stylish'):
    if output_format == 'stylish':
        formatted_diff = stylish.stylize(difference)
        return formatted_diff
    elif output_format == 'plain':
        formatted_diff = plain.get_plain_dict(difference)
        return formatted_diff
    elif output_format == 'json':
        formatted_diff = json.get_json_dict(difference)
        return formatted_diff
