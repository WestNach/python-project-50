from gendiff.parser import open_file


def generate_diff(first_file, second_file):
    file1 = open_file(first_file)
    file2 = open_file(second_file)
    diff = []
    for key in sorted(set(file1.keys()) | set(file2.keys())):
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                diff.append(f"  {key}: {str(file1[key])}")
            else:
                diff.append(f"- {key}: {str(file1[key])}")
                diff.append(f"+ {key}: {str(file2[key])}")
        elif key in file1:
            diff.append(f"- {key}: {str(file1[key])}")
        else:
            diff.append(f"+ {key}: {str(file2[key])}")

    return "{\n" + "\n".join(diff) + "\n}"
