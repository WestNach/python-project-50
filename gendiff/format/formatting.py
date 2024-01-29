from gendiff.format.json import get_json_dict
from gendiff.format.plain import get_plain_dict
from gendiff.format.stylish import stylize


def format_diff(difference, format='stylish'):
    if format == 'stylish':
        formatted_diff = stylize(difference)
        return formatted_diff
    elif format == 'plain':
        formatted_diff = get_plain_dict(difference)
        return formatted_diff
    elif format == 'json':
        formatted_diff = get_json_dict(difference)
        return formatted_diff
