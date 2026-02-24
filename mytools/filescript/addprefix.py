from mytools.resources.argparser import parse_args
import os
from pathlib import Path

def add_prefix_to_directory(directory:Path, prefix:str):
    files = list(filter(lambda f: not f.startswith("."), os.listdir(directory)))

    for file in files:
        os.rename(directory / file, directory / (prefix + file))


def main():
    args, opts = parse_args()
    
    directory = opts.get("dir") or os.getcwd()
    assert len(args) == 1, "Usage: python addprefix.py <prefix>"
    prefix = args[0]

    add_prefix_to_directory(Path(directory), prefix)


if __name__ == "__main__":
    main()