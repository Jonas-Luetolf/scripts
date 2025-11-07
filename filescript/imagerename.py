from pathlib import Path
import os
from datetime import datetime
import platform
import sys

from PIL import Image
from PIL.ExifTags import TAGS


# all filetypes affectet by this script
IMAGE_FILE_TYPES = [".JPG", ".PNG"]
RAW_FILETYPE = ".CR2"


def get_date_taken(file_path):
    """
    gets the date from exif data


    :param file_path path to the file

    :return date in format "YYYY:MM:DD HH:MM:SS"
    """

    image = Image.open(file_path)
    exif_data = image._getexif()

    if exif_data is not None:
        for tag, value in exif_data.items():
            if TAGS.get(tag) == "DateTimeOriginal" and value is not None:
                return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")

        raise AttributeError

    else:
        raise AttributeError


def get_file_creation_date(file_path):
    """
    gets the os file creation date

    :param file path path to the file

    :return date in format "YYYY:MM:DD HH:MM:SS"
    """

    if platform.system() == "Windows":
        return datetime.fromtimestamp(os.path.getctime(file_path))

    else:
        return datetime.fromtimestamp(os.stat(file_path).st_mtime)


def get_image_creation_date(file_path):
    """
    gets the date from exif if exists otherwise it takes the os file creation date

    :param file path path to the file

    :return date in format "YYYY:MM:DD HH:MM:SS"
    """

    try:
        return get_date_taken(file_path)

    except AttributeError:
        date = get_file_creation_date(file_path)
        if date is None:
            raise AttributeError(f"No Date for file {file_path} found")

        return date


def is_image(path: Path):
    """
    checks if the file type is in image typs list
    ignores upper and lower case differences

    :param path path to the file

    :return bool if the type is in the list
    """
    return any(str(path).upper().endswith(ext) for ext in IMAGE_FILE_TYPES)


def main(path: Path, prefix=False, raw=False):
    # get all files in the directory and sort them by creation date
    files = list(filter(is_image, os.listdir(path)))
    files = list(sorted(files, key=lambda x: get_image_creation_date(path / x)))

    # count the files and get the max number lenght
    num_files = len(files)
    num_len = len(str(num_files))

    i = 0
    last_date = ""

    for file in files:
        date = get_image_creation_date(path / file)

        # reset counter if day has changed and prefix is present
        if last_date != date.strftime("%Y%m%d") and prefix:
            last_date = date.strftime("%Y%m%d")
            i = 0

        # format file number to the max number len
        new_name = (
            "0" * (num_len - len(str(i))) + f"{i}{os.path.splitext(file)[-1].lower()}"
        )

        new_name = date.strftime("%Y%m%d") + "_" + new_name

        os.rename(path / file, path / new_name)

        # rename raw file if raw file exists and raw flag is present
        if raw:
            raw_filename = file[::-1].split(".", 1)[1][::-1] + RAW_FILETYPE
            if os.path.exists(raw_filename):
                new_raw_name = new_name[::-1].split(".", 1)[1][::-1] + RAW_FILETYPE
                os.rename(path / raw_filename, path / new_raw_name)
        i += 1


if __name__ == "__main__":
    # command must be of type <path> [--prefix; optional] [--raw; optional]

    # check if script call has a path and all flags are valid
    try:
        assert len(sys.argv) > 2
        assert os.path.isdir(sys.argv[1])
        assert all(flag in ["--raw"] for flag in sys.argv[2:])

    except AssertionError as exc:
        print("Please provide a valid path and flags")
        print(
            "Usage: python imagerename.py <path> [--raw; optional]"
        )
        sys.exit(1)

    path = Path(sys.argv[1])

    # get flags
    if len(sys.argv) > 2:
        flags = sys.argv[2:]
    else:
        flags = []

    main(path, "--prefix" in flags, "--raw" in flags)
