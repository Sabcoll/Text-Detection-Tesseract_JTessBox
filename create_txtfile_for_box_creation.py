# Definiere die Zeichen, die in die Datei geschrieben werden sollen
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,;:!?'\"()"
math_symbols = "+--×÷="

# Füge die mathematischen Symbole zu den normalen Zeichen hinzu
all_characters = characters + math_symbols

# Füge ein Leerzeichen zwischen jedem Zeichen hinzu
spaced_characters = " ".join(all_characters)

# Pfad zur Ausgabedatei festlegen
output_file_path = 'output_with_math_symbols.txt'

# Funktion zum Schreiben der Zeichen in die Datei
def write_characters_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
        print(f'Zeichen wurden erfolgreich in {file_path} geschrieben.')

if __name__ == '__main__':
    write_characters_to_file(output_file_path, spaced_characters)
