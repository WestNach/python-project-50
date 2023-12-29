import json


def generate_diff(first_file, second_file):
    data1 = json.load(open(first_file))
    data2 = json.load(open(second_file))

    diff = []

    for key in sorted(set(data1.keys()) | set(data2.keys())):
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff.append(f"  {key}: {str(data1[key])}")
            else:
                diff.append(f"- {key}: {str(data1[key])}")
                diff.append(f"+ {key}: {str(data2[key])}")
        elif key in data1:
            diff.append(f"- {key}: {str(data1[key])}")
        else:
            diff.append(f"+ {key}: {str(data2[key])}")

    return "{\n" + "\n".join(diff) + "\n}"
