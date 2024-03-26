from .plain import plain_format
from .stylish import stylize
from .json import json_format


def format_diff(differance, output_format='stylish'):
    if output_format == 'stylish':
        formatted_diff = stylize(differance)
        return formatted_diff
    elif output_format == 'plain':
        formatted_diff = plain_format(differance)
        return formatted_diff
    elif output_format == 'json':
        formatted_diff = json_format(differance)
        return formatted_diff
