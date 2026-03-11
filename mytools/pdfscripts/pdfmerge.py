from mytools.resources.argparser import parse_args
import pathlib
from PyPDF2 import PdfMerger


def merge_pdfs(output, inputs):
    merger = PdfMerger()
    for pdf in inputs:
        merger.append(pdf)
    merger.write(output)
    merger.close()

def main():
    args, _ = parse_args()
    assert len(args) >= 3, "At least one output file and two input files are required."

    output = args[0]
    inputs = args[1:]

    assert all(pathlib.Path(inp).suffix.lower() == '.pdf' for inp in inputs), "All input files must be PDF files."

    merge_pdfs(output, inputs)
    print(f"Merged {len(inputs)} files into {output}")


if __name__ == "__main__":
    main()
