import os
import pytesseract
from PIL import Image

def execute_command(command):
    try:
        os.system(command)
        print(f"Befehl erfolgreich ausgeführt: {command}")
    except Exception as e:
        print(f"Fehler bei der Ausführung des Befehls: {command}\n{e}")

def main():
    # Pfad zu Tesseract und anderen benötigten Dateien
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    training_data_path = r'C:\Tesseract\Training'
    font_properties_file = os.path.join(training_data_path, 'font_properties')
    new_font = 'myNewFont'  # Name der neuen Schriftart

    # Sicherstellen, dass das Training-Verzeichnis existiert
    if not os.path.exists(training_data_path):
        os.makedirs(training_data_path)

    # Schritt 1: Box-Dateien manuell mit JTessBoxEditor erzeugen
    # Öffnen Sie Ihre Trainingsbilder in JTessBoxEditor und erstellen Sie die Box-Dateien

    # Schritt 2: Schriftart-Eigenschaften erstellen
    # Erzeugen der Datei font_properties, die Informationen über die Schriftart enthält.
    with open(font_properties_file, 'w') as f:
        f.write(f'{new_font} 0 0 0 0 0')

    # Schritt 3: Training ausführen
    # Führen Sie das Trainingsverfahren mit den manuell erstellten Box-Dateien durch.
    execute_command(f'tesseract {os.path.join(training_data_path, new_font + ".tif")} {new_font} box.train')
    execute_command(f'mftraining -F font_properties -U unicharset -O {os.path.join(training_data_path, new_font + ".unicharset")} {os.path.join(training_data_path, new_font + ".tr")}')
    execute_command(f'cntraining {os.path.join(training_data_path, new_font + ".tr")}')

    # Schritt 4: Trainingsergebnisse zusammenführen
    # Zusammenführen der erzeugten Dateien in eine Datei.
    os.rename('inttemp', os.path.join(training_data_path, new_font + '.inttemp'))
