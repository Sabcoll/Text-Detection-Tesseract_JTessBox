# Importiere die notwendigen Bibliotheken
from PIL import Image
import pytesseract

# Pfad zu Tesseract-OCR festlegen
pytesseract.pytesseract.tesseract_cmd = r'JTessBox\tesseract-ocr\tesseract.exe'

# Funktion zum Auslesen des Textes aus einem Bild
def extract_text(image_path):
    # Bild öffnen
    image = Image.open(image_path)

    # Text mit Tesseract auslesen
    text = pytesseract.image_to_string(image)
    #text = pytesseract.image_to_string(image, config=tesseract_config)
    return text

if __name__ == '__main__':
    # Pfad zum Bild festlegen
    image_path = 'Tesseract\Test\jbgf7chmq8me1.jpeg'
    # Text aus dem Bild auslesen
    text = extract_text(image_path)
    # Ausgelesenen Text anzeigen
    print('Ausgelesener Text:')
    print(text)
