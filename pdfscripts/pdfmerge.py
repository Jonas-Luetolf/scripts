#!/usr/bin/env python3
import sys
import pathlib
from PyPDF2 import PdfMerger

def merge_pdfs(output, inputs):
    merger = PdfMerger()
    for pdf in inputs:
        merger.append(pdf)
    merger.write(output)
    merger.close()

def main():
    if len(sys.argv) < 4:
        print("Usage: python merge_pdfs.py output.pdf input1.pdf input2.pdf [input3.pdf ...]")
        sys.exit(1)

    output = sys.argv[1]
    inputs = sys.argv[2:]
    
    assert all(pathlib.isfile(inp) for inp in inputs), "Not all input files exist."

    merge_pdfs(output, inputs)
    print(f"Merged {len(inputs)} files into {output}")

if __name__ == "__main__":
    main()
