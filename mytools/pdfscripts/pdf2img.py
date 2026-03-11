from mytools.resources.argparser import parse_args
from pdf2image import convert_from_path
import os
from pathlib import Path

def save_pages_as_PNG(file: Path, output_directory: Path):
    pages = convert_from_path(file, dpi=300)

    if len(pages) == 1:
        pages[0].save(f"{file.stem}.png", "PNG")

    else:
        for i, page in enumerate(pages):
            image_filename = Path(output_directory) / f"{file.stem}_page_{i+1}.png"
            page.save(image_filename, "PNG")


def main():
    args, opts = parse_args()
    assert len(args) == 1, "Please provide exactly one PDF file as an argument."

    file = Path(args[0])
    output_directory = opts.get("out") or "./"
    
    save_pages_as_PNG(file, Path(output_directory))


if __name__ == "__main__":
    main()
