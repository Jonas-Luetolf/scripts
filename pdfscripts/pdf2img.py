#!/usr/bin/python3

from pdf2image import convert_from_path
import sys
import os

# Path to your PDF file
assert len(sys.argv) == 2

pdf_path = sys.argv[1].strip()
filename, _ = os.path.splitext(pdf_path)

# Convert PDF to images
pages = convert_from_path(pdf_path, dpi=300)

if len(pages) == 1:
    pages[0].save(f"{filename}.png", "PNG")
else:    
    for i, page in enumerate(pages):
        image_filename = f"{pdf_path}_page_{i+1}.png"
        page.save(image_filename, "PNG")
