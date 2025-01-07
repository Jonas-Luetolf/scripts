import PyPDF2
import sys

def remove_metadata(input_pdf_path, output_pdf_path):
    """
    Entfernt alle Metadaten aus einer PDF-Datei.

    :param input_pdf_path: Pfad zur Eingabe-PDF-Datei
    :param output_pdf_path: Pfad zur Ausgabe-PDF-Datei ohne Metadaten
    """
    try:
        # Öffne die Eingabe-PDF-Datei
        with open(input_pdf_path, 'rb') as input_pdf:
            reader = PyPDF2.PdfReader(input_pdf)
            writer = PyPDF2.PdfWriter()

            # Kopiere alle Seiten in einen neuen Writer
            for page in reader.pages:
                writer.add_page(page)

            # Setze Metadaten auf ein leeres Dictionary
            writer.add_metadata({})

            # Schreibe die Ausgabe-PDF-Datei
            with open(output_pdf_path, 'wb') as output_pdf:
                writer.write(output_pdf)

        print(f"Alle Metadaten wurden erfolgreich aus {input_pdf_path} entfernt und in {output_pdf_path} gespeichert.")

    except Exception as e:
        print(f"Es gab ein Problem beim Entfernen der Metadaten: {e}")

input_pdf_path = sys.argv[1]
output_pdf_path = "no-meta-"+input_pdf_path
remove_metadata(input_pdf_path, output_pdf_path)
