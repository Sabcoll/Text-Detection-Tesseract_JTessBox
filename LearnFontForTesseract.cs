using System;
using System.Diagnostics;
using System.IO;

namespace TesseractTraining
{
    class Program
    {
        static void Main(string[] args)
        {
            // Pfad zu Tesseract und anderen benötigten Dateien
            string tesseractPath = @"..\JTessBox\Tesseract-OCR\tesseract.exe";
            string trainingDataPath = @"..\Tesseract\Training\";
            string fontPropertiesFile = Path.Combine(trainingDataPath, "font_properties");
            string newFont = "Exocet"; // Name der neuen Schriftart

            // Sicherstellen, dass das Training-Verzeichnis existiert
            if (!Directory.Exists(trainingDataPath))
            {
                Directory.CreateDirectory(trainingDataPath);
            }

            // Schritt 1: Box-Dateien manuell mit JTessBoxEditor erzeugen
            // Öffnen Sie Ihre Trainingsbilder in JTessBoxEditor und erstellen Sie die Box-Dateien

            // Schritt 2: Schriftart-Eigenschaften erstellen
            // Erzeugen der Datei font_properties, die Informationen über die Schriftart enthält.
            File.WriteAllText(fontPropertiesFile, $"{newFont} 0 0 0 0 0");

            // Schritt 3: Training ausführen
            // Führen Sie das Trainingsverfahren mit den manuell erstellten Box-Dateien durch.
            ExecuteCommand($"tesseract {Path.Combine(trainingDataPath, newFont + ".tif")} {newFont} box.train");
            ExecuteCommand($"mftraining -F font_properties -U unicharset -O {Path.Combine(trainingDataPath, newFont + ".unicharset")} {Path.Combine(trainingDataPath, newFont + ".tr")}");
            ExecuteCommand($"cntraining {Path.Combine(trainingDataPath, newFont + ".tr")}");

            // Schritt 4: Trainingsergebnisse zusammenführen
            // Zusammenführen der erzeugten Dateien in eine Datei.
            File.Move("inttemp", Path.Combine(trainingDataPath, newFont + ".inttemp"));
            File.Move("pffmtable", Path.Combine(trainingDataPath, newFont + ".pffmtable"));
            File.Move("normproto", Path.Combine(trainingDataPath, newFont + ".normproto"));
            File.Move("shapetable", Path.Combine(trainingDataPath, newFont + ".shapetable"));

            // Schritt 5: Erzeugen der Tessdata-Dateien
            // Kombinieren Sie die Ergebnisse, um die finale .traineddata Datei zu erstellen.
            ExecuteCommand($"combine_tessdata {Path.Combine(trainingDataPath, newFont + ".")}");
        }

        // Hilfsmethode zum Ausführen von Befehlen
        static void ExecuteCommand(string command)
        {
            try
            {
                ProcessStartInfo processInfo = new ProcessStartInfo("cmd.exe", "/c " + command);
                processInfo.CreateNoWindow = true;
                processInfo.UseShellExecute = false;
                processInfo.RedirectStandardError = true;
                processInfo.RedirectStandardOutput =