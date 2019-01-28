import argparse
import os


def remove_boms(all_file_names):
    for file in all_file_names:
        remove_bom(file)


def remove_bom(file_name):
    print(f"Looking for BOM in {file_name}")
    s = open(file_name, mode='r', encoding='utf-8-sig').read()
    open(file_name, mode='w', encoding='utf-8').write(s)


def find_files_with_ext(extension):
    print(f"looking for files with extension {extension}")
    found_files = []
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(f".{extension}"):
                full_name = os.path.join(root, file)
                print(f"found {full_name}")
                found_files.append(full_name)
    return found_files


if __name__ == "__main__":
    parser = argparse.ArgumentParser( description='find all files with extension and remove bom if it exists')
    parser.add_argument("--extension", type=str, default='json', required=False)
    args = parser.parse_args()

    files_to_search = find_files_with_ext(args.extension)
    remove_boms(files_to_search)
