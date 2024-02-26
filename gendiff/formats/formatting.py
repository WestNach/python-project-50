from gendiff.formats.json import get_json_dict
from gendiff.formats.plain import get_plain_dict
from gendiff.formats.stylish import stylize


def format_diff(difference, output_format='stylish'):
    if output_format == 'stylish':
        formatted_diff = stylize(difference)
        return formatted_diff
    elif output_format == 'plain':
        formatted_diff = get_plain_dict(difference)
        return formatted_diff
    elif output_format == 'json':
        formatted_diff = get_json_dict(difference)
        return formatted_diff
