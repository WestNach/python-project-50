def generate_diff(first_file, second_file):
    diff = []
    for key in sorted(set(first_file.keys()) | set(second_file.keys())):
        if key in first_file and key in second_file:
            if first_file[key] == second_file[key]:
                diff.append(f"  {key}: {str(first_file[key])}")
            else:
                diff.append(f"- {key}: {str(first_file[key])}")
                diff.append(f"+ {key}: {str(second_file[key])}")
        elif key in first_file:
            diff.append(f"- {key}: {str(first_file[key])}")
        else:
            diff.append(f"+ {key}: {str(second_file[key])}")

    return "{\n" + "\n".join(diff) + "\n}"
