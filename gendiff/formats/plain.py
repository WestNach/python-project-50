from stylish import format_value


def get_plain_dict(data, root=''):
    result = []
    parent = root
    for key, val in data.items():
        if val['change'] == 'added':
            parent += str(key)
            result.append(
                f"Property '{parent}' was added \
                with value: {format_value(val['value'])}"
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
                f"Property '{parent}' was updated. \
                 From {old_value} to {new_value}"
            )
            parent = root
        elif val['change'] == 'node':
            parent = f"{root}{key}."
            result.append(get_plain_dict(val['children'], parent))
            parent = root
    return '\n'.join(result)
