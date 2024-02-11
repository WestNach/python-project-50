import json
import plain
import stylish


def format_diff(difference, format='stylish'):
    if format == 'stylish':
        formatted_diff = stylish.stylize(difference)
        return formatted_diff
    elif format == 'plain':
        formatted_diff = plain.get_plain_dict(difference)
        return formatted_diff
    elif format == 'json':
        formatted_diff = json.get_json_dict(difference)
        return formatted_diff
