#!/bin/bash

# Prompt for the target directory
read -p "Please enter your local bin directory (default: ~/bin): " TARGET_DIR
TARGET_DIR=${TARGET_DIR:-~/bin}

# Create the directory if it doesn't exist
mkdir -p "$TARGET_DIR"

# Function to copy and rename scripts without extensions
copy_and_rename() {
    for file in "$1"/*; do
        if [[ -f "$file" ]]; then
            # Remove extension (.py or .sh)
            filename=$(basename "$file")
            newname="${filename%.*}"  # Strip the last extension
            cp "$file" "$TARGET_DIR/$newname"
        fi
    done
}

# Copy and rename scripts from the rofi-scripts folder if it exists
if [ -d "rofi-scripts" ]; then
    copy_and_rename "rofi-scripts"
fi

copy_and_rename "filescript"
copy_and_rename "pdfocrpipeline"
copy_and_rename "scientific"

# Make scripts executable
chmod +x "$TARGET_DIR"/*
echo "All scripts have been copied to $TARGET_DIR, renamed without extensions, and made executable."

# Check if the target directory is in PATH
if [[ ":$PATH:" != *":$TARGET_DIR:"* ]]; then
    echo "Warning: $TARGET_DIR is not in your PATH."
    echo "To add it, run the following command:"
    echo "export PATH=\"$TARGET_DIR:\$PATH\""
    echo "To make this change permanent, add the above line to your ~/.bashrc or ~/.zshrc file."
fi
