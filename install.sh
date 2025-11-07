#!/bin/bash
# ================================================================
#  ⚠️ DISCLAIMER
#  This script was generated with the assistance of AI (ChatGPT).
#  It has NOT been fully tested or reviewed for every environment.
#  Use it at your own discretion and review its logic before running
#  on production systems.
# ================================================================

# ============================================
# Dynamic Script Installer
# Copies scripts from subfolders to ~/bin (or user-specified folder)
#
# Features:
# - Dynamically scans folders
# - Skips hidden folders and permanently excluded ones (e.g. venv)
# - Supports inclusion flags (--linux, --linux-minimal, etc.)
# - Supports dynamic exclusions (--no-<folder>)
# - Supports --all to copy everything
# ============================================

# ---------- CONFIGURATION ----------
# Define folders that always require certain flags to be copied
# (space-separated if multiple)
declare -A FLAG_REQUIRED=(
    ["linux"]="--linux --linux-minimal"
    ["rofi-scripts"]="--linux"
)

# Permanent excludes (these folders are always ignored)
EXCLUDED_FOLDERS=("venv" ".git" ".github" ".idea" "__pycache__")

# ---------- USER INPUT ----------
read -p "Please enter your local bin directory (default: ~/bin): " TARGET_DIR
TARGET_DIR=${TARGET_DIR:-~/bin}
mkdir -p "$TARGET_DIR"

# ---------- PARSE FLAGS ----------
FLAGS=("$@")

# Check if a flag is present
has_flag() {
    local flag=$1
    for arg in "${FLAGS[@]}"; do
        if [[ "$arg" == "$flag" ]]; then
            return 0
        fi
    done
    return 1
}

# Check if any of a set of flags is present
has_any_flag() {
    local required_flags=($1)
    for req_flag in "${required_flags[@]}"; do
        if has_flag "$req_flag"; then
            return 0
        fi
    done
    return 1
}

# Check if a folder is permanently excluded
is_permanently_excluded() {
    local folder="$1"
    for excl in "${EXCLUDED_FOLDERS[@]}"; do
        if [[ "$folder" == "$excl" ]]; then
            return 0
        fi
    done
    return 1
}

# Check if a folder is excluded via --no-<folder>
is_dynamically_excluded() {
    local folder="$1"
    local exclude_flag="--no-$folder"
    has_flag "$exclude_flag"
}

# ---------- COPY & RENAME FUNCTION ----------
copy_and_rename() {
    local src_dir="$1"
    for file in "$src_dir"/*; do
        if [[ -f "$file" ]]; then
            filename=$(basename "$file")
            newname="${filename%.*}"  # Remove last extension (.py, .sh, etc.)
            cp "$file" "$TARGET_DIR/$newname"
        fi
    done
}

# ---------- MAIN LOGIC ----------
PARENT_DIR=$(pwd)
ALL_MODE=false

if has_flag "--all"; then
    ALL_MODE=true
fi

echo "Scanning folders in: $PARENT_DIR"
echo ""

for dir in "$PARENT_DIR"/*/; do
    dir=${dir%/}  # remove trailing slash
    folder=$(basename "$dir")

    # Skip hidden directories or permanently excluded ones
    if [[ "$folder" == .* ]] || is_permanently_excluded "$folder"; then
        echo "Skipping (permanently excluded): $folder"
        continue
    fi

    # If --all is active, copy everything
    if $ALL_MODE; then
        echo "Copying (all mode): $folder"
        copy_and_rename "$dir"
        continue
    fi

    # Skip dynamically excluded folders
    if is_dynamically_excluded "$folder"; then
        echo "Skipping (explicitly excluded via --no-$folder): $folder"
        continue
    fi

    # Check inclusion flags
    if [[ -n "${FLAG_REQUIRED[$folder]}" ]]; then
        required_flags="${FLAG_REQUIRED[$folder]}"
        if has_any_flag "$required_flags"; then
            echo "Copying (matched flag): $folder"
            copy_and_rename "$dir"
        else
            echo "Skipping (requires one of: $required_flags): $folder"
        fi
    else
        echo "Copying (no flag required): $folder"
        copy_and_rename "$dir"
    fi
done

# ---------- POST SETUP ----------
chmod +x "$TARGET_DIR"/* 2>/dev/null
echo ""
echo "✅ All scripts have been copied to $TARGET_DIR and made executable."

# ---------- PATH CHECK ----------
if [[ ":$PATH:" != *":$TARGET_DIR:"* ]]; then
    echo ""
    echo "⚠️  Warning: $TARGET_DIR is not in your PATH."
    echo "To add it, run:"
    echo "  export PATH=\"$TARGET_DIR:\$PATH\""
    echo "To make it permanent, add the above line to your ~/.bashrc or ~/.zshrc."
fi
