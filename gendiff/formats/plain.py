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
