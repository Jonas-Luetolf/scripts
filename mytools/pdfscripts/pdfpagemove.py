from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path
from mytools.resources.argparser import parse_args


def parse_page_range(s: str):
    if "-" in s:
        start, end = map(int, s.split("-", 1))
        if start > end:
            raise ValueError("Invalid range: start must be <= end")
        return start - 1, end - 1
    else:
        p = int(s) - 1
        return p, p


def move_pages_in_pdf(input_file: Path, output_file: Path, src_range: str, target_page: int, after: bool = False):
    reader = PdfReader(str(input_file))
    writer = PdfWriter()

    pages = list(reader.pages)

    src_start, src_end = parse_page_range(src_range)

    block = pages[src_start:src_end + 1]
    del pages[src_start:src_end + 1]

    dst = target_page - 1
    if after:
        dst += 1

    # adjust destination if removal happened before it
    if src_start < dst:
        dst -= len(block)

    for i, p in enumerate(block):
        pages.insert(dst + i, p)

    for page in pages:
        writer.add_page(page)

    with open(output_file, "wb") as f:
        writer.write(f)


def main():
    args, opts = parse_args()

    assert len(args) == 3, "Usage: pdf_move <file> <src_page|start-end> <target_page>"

    input_file = Path(args[0])
    src_range = args[1]
    target_page = int(args[2])

    output_file = Path(opts.get("out") or f"{input_file.stem}_reordered.pdf")
    after = bool(opts.get("after"))

    move_pages_in_pdf(input_file, output_file, src_range, target_page, after)


if __name__ == "__main__":
    main()
