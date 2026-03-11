from mytools.resources.argparser import parse_args
import os
from pathlib import Path
import re


def is_valid_filename(file_path: Path) -> bool:
    """
    Check whether a file name starts with a date prefix (YYYYMMDD_).

    Args:
        file_path (Path): Path object representing the file.

    Returns:
        bool: True if the filename matches the expected pattern.
    """
    file_name = file_path.name
    return re.match(r"^\d{8}_\w+", file_name) is not None


def create_file_table(files: list) -> dict:
    """
    Group files by year and month based on their date prefix.

    Args:
        files (list[Path]): List of file paths to organize.

    Returns:
        dict[str, dict[str, list[Path]]]: Nested dictionary structured
        as {year: {month: [files]}}.
    """
    file_table = {}

    for file_path in files:
        if not is_valid_filename(file_path):
            print(file_path)
            continue

        # extract date
        date_str = file_path.name[:8]
        year = date_str[:4]
        month = date_str[4:6]

        # create dict structure
        if year not in file_table:
            file_table[year] = {}

        if month not in file_table[year]:
            file_table[year][month] = []

        file_table[year][month].append(file_path)
    return file_table


def sort_files_by_date(file_table: dict, path: Path) -> None:
    """
    Move files into year/month subdirectories.

    Args:
        file_table (dict): Nested dictionary from create_file_table().
        path (Path): Base directory where folders will be created.
    """
    for year in file_table.keys():
        for month in file_table[year].keys():

            # create path if not exists
            new_path = path / year / month
            new_path.mkdir(parents=True, exist_ok=True)

            for file in file_table[year][month]:
                if not os.path.exists(new_path / file.name):
                    file.rename(new_path / file.name)


def organize_directory(path: Path) -> None:
    """
    Organize files in a directory into year/month folders.

    Args:
        path (Path): Directory containing files to organize.
    """
    files = list(filter(lambda f: f.is_file(), path.iterdir()))
    file_table = create_file_table(files)
    sort_files_by_date(file_table, path)


def main() -> int:
    args, _ = parse_args()

    assert len(args) == 1, "Please provide exactly one directory path"
    path = Path(args[0])
    organize_directory(path)
   
if __name__ == "__main__":
    main()