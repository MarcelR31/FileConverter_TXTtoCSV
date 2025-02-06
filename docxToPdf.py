from docx import Document
from reportlab.pdfgen import canvas
import textwrap

def docx_to_pdf(input_file, output_file):
    try:
        # DOCX-Datei öffnen und Inhalt extrahieren
        doc = Document(input_file)
        paragraphs = [p.text for p in doc.paragraphs]  # Absätze auslesen

        # PDF erstellen
        pdf = canvas.Canvas(output_file)
        text_object = pdf.beginText(100, 780)  # Textstartpunkt setzen
        text_object.setFont("Helvetica", 10)  # Schriftart und -größe festlegen

        # Textumbruch konfigurieren
        max_width = 80  # Maximale Zeichen pro Zeile
        wrapper = textwrap.TextWrapper(width=max_width)

        # Text zeilenweise schreiben
        for paragraph in paragraphs:
            if paragraph.strip():  # Nur nicht-leere Absätze verarbeiten
                wrapped_lines = wrapper.wrap(paragraph)  # Absatz umbrechen
                for wrapped_line in wrapped_lines:
                    text_object.textLine(wrapped_line)  # Zeile schreiben
                text_object.textLine("")  # Leerzeile nach jedem Absatz hinzufügen

        pdf.drawText(text_object)
        pdf.save()

        print(f"Erfolgreich konvertiert: {output_file}")
    except Exception as e:
        print(f"Fehler bei der Umwandlung: {e}")