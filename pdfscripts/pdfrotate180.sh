#!/bin/bash

# Rotate all pages of a PDF by 180 degrees
# Usage: ./pdf_turn.sh input.pdf

if [ -z "$1" ]; then
    echo "Usage: $0 input.pdf"
    exit 1
fi

INPUT="$1"
TMPFILE=$(mktemp /tmp/rotated.XXXXXX.pdf)

# Rotate every page 180° using qpdf
qpdf "$INPUT" --rotate=180:1-z "$TMPFILE"

# Overwrite the original PDF
mv "$TMPFILE" "$INPUT"

echo "✅ Rotated all pages by 180° in: $INPUT"

