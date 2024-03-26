import json


def json_format(diff: dict):
    return json.dumps(diff, indent=4)
