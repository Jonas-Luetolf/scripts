from mytools.resources.argparser import parse_args
import os

def rename_files_in_directory(directory, suffix=""):
    files = list(filter(lambda f: not f.startswith("."), os.listdir(directory)))

    for file in files:
        new_name = input(f"new name for {file}: ")

        if new_name != "":
            os.rename(file, suffix + new_name + os.path.splitext(file)[1])

def main():
    _, opts = parse_args()
    print("press ENTER to skip file")

    suffix = opts["suffix"] if "suffix" in opts else ""
    rename_files_in_directory(os.getcwd(), suffix)


if __name__ == "__main__":
    main()
