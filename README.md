# scripts

My personal collection of small but useful scripts for file management and general automation tasks.

## Install

Manually download Repo and build using pip:

```bash
git clone https://github.com/Jonas-Luetolf/scripts.git
pip install -e .
```

## File and Directory Utilities

| Script             | Description                                                                                                                       |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| **addprefix**      | Adds a prefix to all filenames in the specified directory.                                                                        |  |
| **filenumberer**   | Numbers all files in a directory.                                                                                                 |
| **rename**         | Helps you rename all files in a directory, allowing suffix customization.                                                         |
| **dateprefixsort** | Sorts all files whose names start with a date (`YYYYMMDD`) into corresponding folders.                                            |
| **imagerename**    | Renames image files based on EXIF or file creation date to `YYYYMMDD_<img_number_per_day>` `--raw` flag renames both the .JPG and .CR2 file.                                  |
| **video2frames**   | Extracts frames from a video file and saves them as images.                                                                       |


## Grafics Tools
| Script             | Description                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------- |
| **confettigen**    | Generates a quadratic SVG with some randomly generated confetti.                              |


---

## PDF Tools

| Script           | Description                                                                    |
| ---------------- | ------------------------------------------------------------------------------ |
| **pdf2img**      | Converts PDF to image file.                                                    |
| **pdfocr**       | Runs OCR (Optical Character Recognition) on PDF files to make them searchable. |
| **pdfrmmeta**    | Removes all metadata from a PDF file.                                          |
| **pdfmerge**     | Merges multiple PDF files into a single PDF.                                   |
| **pdfpagemove**  | Moves a specific page or range of pages in a PDF file to a new position.       |
---

## Scientific

| Script          | Description                                            |
| --------------- | ------------------------------------------------------ |
| **truth-table** | Generates a truth table for boolean logic expressions. |

---

## Other

| Script     | Description                                        |
| ---------- | -------------------------------------------------- |
| **easter** | Calculates the date of Easter for a specific year. |


⚠️ Disclaimer

Some scripts in this repository were written with the help of AI and may not have been fully tested.
Use them at your own risk. Always review scripts before running them, especially those that modify files, directories.
