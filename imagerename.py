from pathlib import Path
import os
from datetime import datetime
import platform
import sys

from PIL import Image
from PIL.ExifTags import TAGS


# all filetypes affectet by this script
IMAGE_FILE_TYPES = [".JPG", ".PNG"]


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


def main(path: Path, prefix=False):
    files = list(filter(is_image, os.listdir(path)))
    files = list(sorted(files, key=lambda x: get_image_creation_date(path / x)))

    num_files = len(files)
    num_len = len(str(num_files))

    i = 0
    last_date = ""

    for file in files:
        date = get_image_creation_date(path / file)

        # reset counter if day has changed
        if last_date != date.strftime("%Y%m%d") and prefix:
            last_date = date.strftime("%Y%m%d")
            i = 0

        # format file number to the max number len
        new_name = (
            "0" * (num_len - len(str(i))) + f"{i}{os.path.splitext(file)[-1].lower()}"
        )

        # add prefix to the name
        if prefix:
            new_name = date.strftime("%Y%m%d") + "_" + new_name

        os.rename(path / file, path / new_name)

        i += 1


if __name__ == "__main__":
    # command must be of type <path> [--prefix; optional]
    main(Path(sys.argv[1]), (len(sys.argv) > 2 and sys.argv[2] == "--prefix"))
