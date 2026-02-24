#!/usr/bin/env python3
import os
import toml

# --------------- Konfiguration ----------------
SRC_DIR = "mytools"  # Root deines Pakets
TOML_FILE = "pyproject.toml"
IGNORES = ["__init__.py", "resources"]  # Ordner/Dateien die keine CLI sind
# ----------------------------------------------

def snake_case(name: str) -> str:
    """Konvertiert Dateinamen zu CLI-Befehlen"""
    return name.replace("_", "-")

def find_scripts() -> dict:
    """Finde alle CLI-Scripts unter SRC_DIR"""
    entries = {}
    for root, dirs, files in os.walk(SRC_DIR):
        if "resources" in root:
            continue
        for f in files:
            if not f.endswith(".py") or f in IGNORES:
                continue
            path = os.path.relpath(os.path.join(root, f), SRC_DIR)
            module = path.replace(os.sep, ".")[:-3]  # Entferne .py
            cmd = snake_case(os.path.basename(f)[:-3])
            entries[cmd] = f"mytools.{module}:main"
    return entries

def update_pyproject(scripts: dict):
    """Schreibt die Scripts direkt in pyproject.toml"""
    with open(TOML_FILE, "r", encoding="utf-8") as f:
        data = toml.load(f)

    # Setze die Section [project.scripts]
    data.setdefault("project", {})
    data["project"]["scripts"] = scripts

    with open(TOML_FILE, "w", encoding="utf-8") as f:
        toml.dump(data, f)

    print(f"Updated {TOML_FILE} with {len(scripts)} scripts.")

if __name__ == "__main__":
    scripts = find_scripts()
    update_pyproject(scripts)