# scripts

My personal collection of small but useful scripts for Linux and general automation tasks.
Some are general-purpose, others are tailored for Linux or for use with [rofi](https://github.com/davatorium/rofi).

## Installation

### Prerequisites
* Most scripts are written in python3: Ensure you have python3 installed.
* For rofi-based scripts: `rofi` installed and available in your `$PATH`.
* `bash` or another POSIX-compatible shell.
* Python scripts may require additional packages. A requirements.txt file is provided for all Python dependencies.

### Install Steps

Clone the repository and run the installer:

```bash
git clone https://github.com/Jonas-Luetolf/scripts.git
cd scripts
chmod +x install.sh
./install.sh [FLAGS]
```

This will install the scripts to your system (default behavior depends on the flags provided).

---

## Available Flags (from `install.sh`)

| Flag              | Description                                                                                                                 |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `--linux`         | Installs the Linux-specific scripts (those in `linux` and `rofi-scripts`).                                                  |
| `--linux-minimal` | Installs a reduced set of Linux scripts (only scripts in linux and rofi-scripts excluded).                                        |
| `--all`           | Installs **all scripts**, including `linux` and `rofi-scripts`.                                                             |
| `--no-<folder>`   | Excludes a specific folder from installation. Example: `--no-other` skips installing other folder. |

---

## Example Installs

Install all scripts for Linux (including rofi tools):

```bash
./install.sh --linux
```

Install only minimal Linux scripts (no rofi dependencies):

```bash
./install.sh --linux-minimal
```


## File and Directory Utilities

| Script             | Description                                                                                                                       |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| **addprefix**      | Adds a prefix to all filenames in the specified directory.                                                                        |  |
| **filenumberer**   | Numbers all files in a directory.                                                                                                 |
| **rename**         | Helps you rename all files in a directory, allowing suffix customization.                                                         |
| **dateprefixsort** | Sorts all files whose names start with a date (`YYYYMMDD`) into corresponding folders.                                            |
| **imagerename**    | Renames image files based on EXIF or file creation date to `YYYYMMDD_<img_number_per_day>` `--raw` flag renames both the .JPG and .CR2 file.                                  |
| **video2frames** | Extracts frames from a video file and saves them as images.                    |

---

## PDF Tools

| Script           | Description                                                                    |
| ---------------- | ------------------------------------------------------------------------------ |
| **pdf2img**      | Converts PDF to image file.                          |
| **pdfocr**       | Runs OCR (Optical Character Recognition) on PDF files to make them searchable. |
| **pdfrotate180** | Rotates all pages in a PDF file by 180°.                                       |
| **pdfrmmeta**    | Removes all metadata from a PDF file.                                          |

---

## Rofi Scripts (Linux)

*(Require `rofi` to be installed.)*

| Script       | Description                                                                                             |
| ------------ | ------------------------------------------------------------------------------------------------------- |
| **nm-menu**  | Opens a rofi-based Wi-Fi selection menu to connect to networks (auto-prompts for password if required). |
| **roficalc** | A rofi-powered calculator for quick calculations.                                                       |
| **ssh-menu** | Quickly connect to known SSH hosts through rofi.                                                        |
| **search**   | Opens a rofi prompt for searching the web via your default browser.                                     |

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
