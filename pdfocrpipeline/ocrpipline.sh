#!/usr/bin/env bash

set -euo pipefail

usage() {
    echo "Usage: $0 [--no-keywords] <pdf_file>"
    exit 1
}

GENERATE_KEYWORDS=true

if [ "$#" -lt 1 ]; then
    usage
fi

if [ "$1" == "--no-keywords" ]; then
    GENERATE_KEYWORDS=false
    shift
fi

if [ "$#" -ne 1 ]; then
    usage
fi

PDF_FILE="$1"
TMP_FILE="$(mktemp --suffix=.pdf)"

pdfocr "$PDF_FILE" "$TMP_FILE"
mv "$TMP_FILE" "$PDF_FILE"

if [ "$GENERATE_KEYWORDS" = true ]; then
    pdfkeywords "$PDF_FILE"
fi
