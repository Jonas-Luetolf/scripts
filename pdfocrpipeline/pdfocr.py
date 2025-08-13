#!/bin/python3
import os
import sys
import subprocess
import fitz
from pdf2image import convert_from_path


def ocr_pdf(input_pdf: str, output_pdf: str, lang: str = "deu", dpi: int = 300) -> None:
    """Perform OCR on a PDF and save the output as a searchable PDF."""
    temp_dir = os.path.expanduser("~/.local/share/orca-slicer/ocr-temp/")
    os.makedirs(temp_dir, exist_ok=True)

    # Convert PDF pages to images
    images = convert_from_path(input_pdf, dpi=dpi, output_folder=temp_dir, fmt='png')
    image_files = sorted([os.path.join(temp_dir, f) for f in os.listdir(temp_dir) if f.endswith(".png")])

    ocr_pdfs = []
    for i, img_path in enumerate(image_files):
        out_base = os.path.join(temp_dir, f"page_{i+1}")
        subprocess.run([
            "tesseract", img_path, out_base,
            "-l", lang, "pdf"
        ], check=True)
        ocr_pdfs.append(out_base + ".pdf")

    # Merge OCR PDFs
    merged_doc = fitz.open()
    for pdf_file in ocr_pdfs:
        merged_doc.insert_pdf(fitz.open(pdf_file))

    merged_doc.save(output_pdf)
    merged_doc.close()

    # Remove temporary files
    for f in os.listdir(temp_dir):
        os.remove(os.path.join(temp_dir, f))
    os.rmdir(temp_dir)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_pdf> <output_pdf>")
        sys.exit(-1)

    input_pdf_path = sys.argv[1]
    output_pdf_path = sys.argv[2]

    ocr_pdf(input_pdf_path, output_pdf_path)
