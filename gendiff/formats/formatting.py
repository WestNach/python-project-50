import json
from itertools import chain


REPLACER = ' '
DEPTH = 0
SPACES_COUNT = 4


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def get_stylish_output(data, depth=DEPTH):
    if not isinstance(data, dict):
        return format_value(data)
    indent_size = depth + SPACES_COUNT
    indent = REPLACER * indent_size
    current_indent = REPLACER * depth
    indent_before_changed_key = indent[2:]
    result = []
    for key, val in data.items():
        if isinstance(val, dict) and 'change' in val:
            if val['change'] == 'added':
                result.append(
                    f"{indent_before_changed_key}+ {key}: "
                    f"{get_stylish_output(val['value'], indent_size)}"
                )
            elif val['change'] == 'node':
                result.append(
                    f"{indent_before_changed_key}  {key}: "
                    f"{get_stylish_output(val['children'], indent_size)}"
                )
            elif val['change'] == 'updated':
                old_val = format_value(val['old_value'])
                result.append(
                    f"{indent_before_changed_key}- {key}: "
                    f"{get_stylish_output(old_val, indent_size)}"
                )
                new_val = format_value(val['new_value'])
                result.append(
                    f"{indent_before_changed_key}+ {key}: "
                    f"{get_stylish_output(new_val, indent_size)}"
                )
            elif val['change'] == 'deleted':
                result.append(
                    f"{indent_before_changed_key}- {key}: "
                    f"{get_stylish_output(val['value'], indent_size)}"
                )
            elif val['change'] == 'unchanged':
                result.append(
                    f"{indent_before_changed_key}  {key}: "
                    f"{get_stylish_output(val['value'], indent_size)}"
                )
        else:
            new_val = format_value(val)
            result.append(
                f"{indent}{key}: "
                f"{get_stylish_output(new_val, indent_size)}"
            )
    result = chain(['{'], result, [current_indent + '}'])
    return '\n'.join(result)


def stylize(dif):
    output = get_stylish_output(dif)
    return output


def get_plain_dict(data, root=''):
    result = []
    parent = root
    for key, val in data.items():
        if val['change'] == 'added':
            parent += str(key)
            result.append(
                f"Property '{parent}' was added "
                f"with value: {format_value(val['value'])}"
            )
            parent = root
        elif val['change'] == 'deleted':
            parent += str(key)
            result.append(f"Property '{parent}' was removed")
            parent = root
        elif val['change'] == 'updated':
            parent += str(key)
            old_value = format_value(val.get('old_value'))
            new_value = format_value(val.get('new_value'))
            result.append(
                f"Property '{parent}' was updated. "
                f"From {old_value} to {new_value}"
            )
            parent = root
        elif val['change'] == 'node':
            result.extend(get_plain_dict(val['children'], root=f"{root}{key}."))
    return result


def format_diff(difference, output_format='stylish'):
    if output_format == 'stylish':
        formatted_diff = stylize(difference)
        return formatted_diff
    elif output_format == 'plain':
        formatted_diff = get_plain_dict(difference)
        return formatted_diff
    elif output_format == 'json':
        formatted_diff = json.dumps(difference, indent=4)
        return formatted_diff
