from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, Transformation
from mytools.resources.argparser import parse_args


A4_PORTRAIT = (595.28, 841.89)
A4_LANDSCAPE = (841.89, 595.28)


def is_valid_pdf(path: Path) -> bool:
    return path.exists() and path.is_file() and path.suffix.lower() == ".pdf"


def resolve_output_path(input_path: Path, output_arg: str | None) -> Path:
    if output_arg:
        return Path(output_arg)
    return input_path.with_name(input_path.stem + "_a4.pdf")


def process_page(page):
    width = float(page.mediabox.width)
    height = float(page.mediabox.height)

    if width > height:
        target_w, target_h = A4_LANDSCAPE
    else:
        target_w, target_h = A4_PORTRAIT

    scale = min(target_w / width, target_h / height)

    scaled_w = width * scale
    scaled_h = height * scale

    tx = (target_w - scaled_w) / 2
    ty = (target_h - scaled_h) / 2

    page.add_transformation(
        Transformation().scale(scale).translate(tx, ty)
    )

    page.mediabox.lower_left = (0, 0)
    page.mediabox.upper_right = (target_w, target_h)

    return page


def resize_pdf(input_path: Path, output_path: Path) -> None:
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(process_page(page))

    with open(output_path, "wb") as f:
        writer.write(f)


def main() -> int:
    args, opts = parse_args()

    if len(args) != 1:
        print("Usage: pdfresizeA4 <input.pdf> [--out output.pdf]")
        return 1

    input_path = Path(args[0])
    output_path = resolve_output_path(input_path, opts.get("out"))

    if not is_valid_pdf(input_path):
        print(f"Invalid PDF: {input_path}")
        return 1

    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(process_page(page))

    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"Saved: {output_path}")
    return 0


if __name__ == "__main__":
    main()
