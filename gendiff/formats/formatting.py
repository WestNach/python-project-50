import json
from itertools import chain


REPLACER = '  '
INDENT = '    '


def format_style_value(value, depth):
    if isinstance(value, dict):
        result = []
        for key, value in value.items():
            space = INDENT * (depth + 1)
            result.append(f"\n{space}{key}:"
                          f" {format_style_value(value, depth + 1)}")
        line = chain('{', result, '\n', [INDENT * depth, '}'])
        return ''.join(line)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def build_line(data, key, depth, INDENT='  '):
    return f"{'  ' * depth}{INDENT}{data['key']}: " \
           f"{format_style_value(data[key], depth + 1)}"


def get_style_output(node, depth=0):
    lines = []
    space = REPLACER * (depth + 1)
    for value in node.values():
        if value['operation'] == 'nested':
            lines.append(f"{space * 2}{value['key']}: "
                         f"{get_style_output(value['value'], depth + 1)}")
            continue
        if value['operation'] == 'changed':
            lines.append(f"{space}{build_line(value, 'old', depth, '- ')}")
            lines.append(f"{space}{build_line(value, 'new', depth, '+ ')}")
            continue
        if value['operation'] == 'removed':
            lines.append(f"{space}{build_line(value, 'value', depth, '- ')}")
            continue
        if value['operation'] == 'added':
            lines.append(f"{space}{build_line(value, 'value', depth, '+ ')}")
            continue
        if value['operation'] == 'unchanged':
            lines.append(f"{space}{build_line(value, 'value', depth)}")
            continue
    result = chain('{', lines, [INDENT * depth + '}'])
    return "\n".join(result)


def stylize(diff):
    output = get_style_output(diff)
    return output


def format_plain_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, int):
        return value
    return f"'{value}'"


def get_plain_output(node, path=''):
    result = []
    for key, val in node.items():
        current_path = f"{path}{key}"
        start_line = f"Property '{current_path}'"
        operation = val.get('operation')
        if operation == 'changed':
            result.append(f"{start_line} was updated. "
                          f"From {format_plain_value(val['old'])}"
                          f" to {format_plain_value(val['new'])}")
        elif operation == 'nested':
            result.append(get_plain_output(val['value'], current_path + '.'))
        elif operation == 'removed':
            result.append(f"{start_line} was removed")
        elif operation == 'added':
            result.append(f"{start_line} was added "
                          f"with value: {format_plain_value(val['value'])}")
    return '\n'.join(result)


def plain_format(diff_result: dict):
    return get_plain_output(diff_result)


def format_diff(differance, output_format='stylish'):
    if output_format == 'plain':
        formatted_diff = plain_format(differance)
        return formatted_diff
    elif output_format == 'stylish':
        formatted_diff = stylize(differance)
        return formatted_diff
    elif output_format == 'json':
        formatted_diff = json.dumps(differance, indent=4)
        return formatted_diff
