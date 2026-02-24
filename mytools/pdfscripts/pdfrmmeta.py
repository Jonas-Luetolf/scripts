from mytools.resources.argparser import parse_args
import PyPDF2
from pathlib import Path


def remove_metadata(input_pdf_path:Path, output_pdf_path:Path) -> None:
    """
    Removes all metadata from the given PDF file

    Args:
        input_pdf_path (Path): Path to the input PDF file
        output_pdf_path (Path): Output PDF path
    """
    with open(input_pdf_path, 'rb') as input_pdf:
        reader = PyPDF2.PdfReader(input_pdf)
        writer = PyPDF2.PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.add_metadata({})

        with open(output_pdf_path, 'wb') as output_pdf:
            writer.write(output_pdf)


def main():
    args, _ = parse_args()

    assert len(args) == 1, "Usage: pdfrmmeta <input PDF file>"
    
    input_pdf_path = args[0]
    assert Path(input_pdf_path).is_file(), "PDF file does not exists"
    assert Path(input_pdf_path).suffix.lower() == ".pdf", "The specified File has to be a PDF (.pdf) file"

    output_pdf_path = "no-meta-"+input_pdf_path

    remove_metadata(input_pdf_path, output_pdf_path)


if __name__ == "__main__":
    main()
