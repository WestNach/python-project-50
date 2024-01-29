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
            match val['change']:
                case 'added':
                    result.append(
                        f"{indent_before_changed_key}+ {key}: "
                        f"{get_stylish_output(val['value'], indent_size)}"
                    )
                case 'node':
                    result.append(
                        f"{indent_before_changed_key}  {key}: "
                        f"{get_stylish_output(val['children'], indent_size)}"
                    )
                case 'updated':
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
                case 'deleted':
                    result.append(
                        f"{indent_before_changed_key}- {key}: "
                        f"{get_stylish_output(val['value'], indent_size)}"
                    )
                case 'unchanged':
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
    result = chain('{', result, [current_indent + '}'])
    return '\n'.join(result)


def stylize(dif):
    output = get_stylish_output(dif)
    return output
