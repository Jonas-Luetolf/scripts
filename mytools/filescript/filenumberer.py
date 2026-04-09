from os import listdir, rename, getcwd
from os.path import isfile
from sys import argv
from pathlib import Path

from mytools.resources.argparser import parse_args


def get_filetype(filename: str):
    filename = "".join(list(reversed(filename)))
    return ("".join(list(reversed(filename[0 : filename.find(".") + 1])))).lower()


def get_filename(index, name_len):
    zeros = "0" * int(name_len - len(str(index)))
    return zeros + str(index)


def number_files(path, offset=0):
    files = [f for f in listdir(path) if isfile(path / f)]
    files.sort()

    name_len = len(str(len(files)))
    new_names = [
        f"{get_filename(index + offset,name_len)}{get_filetype(name)}"
        for index, name in enumerate(files)
    ]

    for original, new in zip(files, new_names):
        print(f"{original} -> {new}")

    if input("This are the new filenames, do you want to continue? (y|N)") == "y":
        for original, new in zip(files, new_names):
            print(f"Renaming {original} to {new}")
            rename(path / original, path / new)


def main():
    args, opts = parse_args(argv[1:])

    path = Path(args[0]) if len(args) > 0 else Path(getcwd())
    offset = int(opts["offset"]) if "offset" in opts else 0

    number_files(Path(path), offset)


if __name__ == "__main__":
    main()
