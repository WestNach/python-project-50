from json import get_json_dict
from plain import get_plain_dict
import stylish


def format_diff(difference, format='stylish'):
    if format == 'stylish':
        formatted_diff = stylish.stylize(difference)
        return formatted_diff
    elif format == 'plain':
        formatted_diff = get_plain_dict(difference)
        return formatted_diff
    elif format == 'json':
        formatted_diff = get_json_dict(difference)
        return formatted_diff
