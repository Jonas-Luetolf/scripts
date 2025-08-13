#!/bin/python3
import fitz
import subprocess
import json
import os
import re
import sys

TAGS_FILE = os.path.expanduser("~/.local/share/ocr_pipeline/tags.json")
DOC_TYPES_FILE = os.path.expanduser("~/.local/share/ocr_pipeline/document_types.json")

def add_keywords_to_pdf(pdf_path, tags):
    doc = fitz.open(pdf_path)

    metadata = doc.metadata

    old_keywords = metadata.get("keywords", "")
    old_keywords_set = set(k.strip() for k in old_keywords.split(",") if k.strip())

    new_keywords_set = old_keywords_set.union(set(tags))
    new_keywords_str = ", ".join(sorted(new_keywords_set))

    metadata["keywords"] = new_keywords_str
    doc.set_metadata(metadata)

    doc.save(pdf_path, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    doc.close()
    return full_text


def load_tags():
    if os.path.exists(TAGS_FILE):
        with open(TAGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_tags(tags_dict):
    with open(TAGS_FILE, "w", encoding="utf-8") as f:
        json.dump(tags_dict, f, ensure_ascii=False, indent=2)


def load_document_types():
    if os.path.exists(DOC_TYPES_FILE):
        with open(DOC_TYPES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

def build_prompt(text, old_tags, document_types, max_tags=5):
    doc_types_str = ", ".join(document_types)

    old_tags_list = sorted(old_tags.items(), key=lambda x: x[1], reverse=True)
    old_tags_top = [tag for tag, count in old_tags_list[:40]]
    old_tags_str = ", ".join(old_tags_top)

    prompt = f"""
Du bist ein hilfreicher Assistent für die automatische Dokumentenanalyse.

Gegeben ist der vollständige Text eines Dokuments:

{text}

Die möglichen Dokumenttypen sind: {doc_types_str}.

Folgende Tags wurden in früheren Dokumenten häufig verwendet und sollen bei der Standardisierung berücksichtigt werden:
{old_tags_str}

Deine Aufgabe:
- Erstelle eine Liste von 1 bis maximal {max_tags} prägnanten, aussagekräftigen Schlagwörtern (Tags), die den Inhalt, den Dokumenttyp sowie relevante Entitäten (z.B. Personen, Unternehmen, Behörden) des Dokuments treffend beschreiben.
- Wähle dabei genau einen Dokumenttyp als Tag aus, niemals mehr als einen.
- Versuche, relevante Organisationen, Unternehmen, die im Text vorkommen (z.B. Name eines Unternehmens, "Kanton xxx", "Bund") als eigene Tags aufzunehmen.
- Berücksichtige möglichst die Standardisierung anhand der bereits bekannten Tags.
- Tags müssen in der Sprache des Dokuments sein.
- Verwende kurze, prägnante Tags ohne erklärenden Text.

Antworte ausschließlich als Liste im folgenden Format, OHNE zusätzliche Erklärungen oder Text:

[tag1, tag2, tag3, ...]

Beispiel:
["Rechnungswesen", "Kanton Zürich", "Finanzbericht"]
"""

    return prompt.strip()


def ollama_chat(prompt, model="llama3:8b"):
    try:
        result = subprocess.run(
            ["ollama", "run", model, prompt],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError:
        return ""


def parse_tags_from_response(response):
    match = re.search(r"\[(.*?)\]", response)
    if not match:
        return []
    content = match.group(1)
    tags = [tag.strip().strip('"').strip("'") for tag in content.split(",")]
    return [tag for tag in tags if tag]


def update_tags(old_tags, new_tags):
    for tag in new_tags:
        old_tags[tag] = old_tags.get(tag, 0) + 1
    return old_tags


def main(pdf_path):
    full_text = extract_text_from_pdf(pdf_path)
    max_len = 2000
    if len(full_text) > max_len:
        full_text = full_text[:max_len]

    old_tags = load_tags()
    document_types = load_document_types()

    prompt = build_prompt(full_text, old_tags, document_types)

    response = ollama_chat(prompt)

    new_tags = parse_tags_from_response(response)
    if new_tags:
        updated_tags = update_tags(old_tags, new_tags)
        save_tags(updated_tags)
        print(f"[{', '.join(f'\"{tag}\"' for tag in new_tags)}]")

        add_keywords_to_pdf(pdf_path, new_tags)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(-1)

    main(sys.argv[1])
