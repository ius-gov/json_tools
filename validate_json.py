import json
import os

invalid_json_files = []
valid_json_files = []
read_json_files = []


def parse_file(directory, file_name):
    full_path = os.path.join(directory, file_name)
    with open(full_path) as json_file:
        read_json_files.append(full_path)
        try:
            json.load(json_file)
            valid_json_files.append(full_path)
        except ValueError as e:
            print(f"JSON object issue:{full_path} {str(e)}")
            invalid_json_files.append(full_path)


def parse_directory(path: str):
    try:
        for dirpath, dirfiles, files in os.walk(path):
            for file in files:
                if file.endswith(".json"):
                    parse_file(dirpath, file)
    except PermissionError as e:
        print(f"cannot access {str(e)}")


parse_directory('.')
print()
print("Read Files:")
print(read_json_files, len(read_json_files))
print()
print("Valid Files:")
print(valid_json_files, len(valid_json_files))
print()
print("Invalid Files:")
print(invalid_json_files, len(invalid_json_files))
if len(invalid_json_files) > 0:
    print("##vso[task.logissue type=error;]", invalid_json_files)
    exit(1)
