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
