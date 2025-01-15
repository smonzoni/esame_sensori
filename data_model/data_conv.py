import csv

def remove_last_300_rows(input_file, output_file):
    try:
        # Leggi tutte le righe dal file originale
        with open(input_file, 'r', newline='', encoding='utf-8') as csv_file:
            rows = list(csv.reader(csv_file))

        # Rimuovi le ultime 300 righe
        trimmed_rows = rows[:-300] if len(rows) > 300 else []

        # Scrivi le righe rimanenti nel nuovo file
        with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(trimmed_rows)

        print(f"Operazione completata. File salvato come: {output_file}")
    except Exception as e:
        print(f"Errore durante l'elaborazione: {e}")

# Esempio di utilizzo
input_file = 'EB-71-55-86-18-D4_run-4.csv'  # Sostituisci con il nome del tuo file
output_file = 'EB-71-55-86-18-D4_run-6.csv'  # Sostituisci con il nome del file da creare

remove_last_300_rows(input_file, output_file)