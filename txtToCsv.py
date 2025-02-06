import csv

def txt_to_csv(input_file, output_file):
    try:
        with open(input_file, "r") as txt_file, open(output_file, "w", newline="") as csv_file: #r = read; w = write
            writer = csv.writer(csv_file) # CSV schreiber 
            for line in txt_file:
                writer.writerow([line.strip()])  # Jede Zeile in die CSV schreiben. Erwartet Liste
        print(f"Erfolgreich konvertiert: {output_file}")
    except Exception as e:
        print(f"Fehler bei der Umwandlung: {e}")