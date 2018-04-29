# Import - Modul: os
import os

# Import - Modul: configparser
import configparser

# Import - Modul: Variablen
from Konfiguration import Variablen

def programmkonfiguration_laden():
    # Pfad - Programmkonfiguration festlegen
    Pfad_Programmkonfiguration = 'Konfiguration'

    # Bezeichnung - Datei - Programmkonfiguration festlegen
    Bezeichnung_Datei_Programmkonfiguration = '__ProgKonf__.ini'

    # Pruefen, ob die Datei: __ProgKonf__.ini vorhanden ist
    if (os.path.exists(os.path.join(Variablen.Pfad_Grundverzeichnis, Pfad_Programmkonfiguration, Bezeichnung_Datei_Programmkonfiguration))):
        # Programmkonfiguration festlegen
        Programmkonfiguration = []

        # Konfiguration festlegen
        Konfiguration = configparser.ConfigParser()

        # Konfiguration lesen
        Konfiguration.read(os.path.join(Variablen.Pfad_Grundverzeichnis, Pfad_Programmkonfiguration, Bezeichnung_Datei_Programmkonfiguration))

        # Versuch: Programmeigenschaften festzulegen
        try:
            # Versionsnummer festlegen
            Versionsnummer = Konfiguration['Allgemein']['Versionsnummer']

            # Programmsprache festlegen
            Programmsprache = int(Konfiguration['Allgemein']['Programmsprache'])

            # Status - Debug festlegen
            Status_Debug = bool(int(Konfiguration['Allgemein']['Status_Debug']))

            # Status - Vollbild festlegen
            Status_Vollbild = bool(int(Konfiguration['Grafik']['Status_Vollbild']))

            # Max - FPS festlegen
            Max_FPS = int(Konfiguration['Grafik']['Max_FPS'])

            # Fenstergroesse festlegen
            Fenstergroesse = (int(Konfiguration['Grafik']['Fensterbreite']), int(Konfiguration['Grafik']['Fensterhoehe']))

            # Kachelgroesse festlegen
            Kachelgroesse = int(Konfiguration['Grafik']['Kachelgroesse'])

            # IP - Adresse festlegen
            IP_Adresse = Konfiguration['Netzwerk']['IP_Adresse']

            # Port festlegen
            Port = int(Konfiguration['Netzwerk']['Port'])

            # Paketgroesse festlegen
            Paketgroesse = int(Konfiguration['Netzwerk']['Paketgroesse'])

            # Lizenz festlegen
            Lizenz = Konfiguration['Rechte']['Lizenz']

            # Herausgeber festlegen
            Herausgeber = Konfiguration['Rechte']['Herausgeber']
        except:
            # Versionsnummer festlegen
            Versionsnummer = None

            # Programmsprache festlegen
            Programmsprache = None

            # Status - Debug festlegen
            Status_Debug = None

            # Status - Vollbild festlegen
            Status_Vollbild = None

            # Max - FPS festlegen
            Max_FPS = None

            # Fenstergroesse festlegen
            Fenstergroesse = None

            # Kachelgroesse festlegen
            Kachelgroesse = None

            # IP - Adresse festlegen
            IP_Adresse = None

            # Port festlegen
            Port = None

            # Paketgroesse festlegen
            Paketgroesse = None

            # Lizenz festlegen
            Lizenz = None

            # Herausgeber festlegen
            Herausgeber = None

        # Programmkonfiguration festlegen
        Programmkonfiguration.append(Versionsnummer)
        Programmkonfiguration.append(Programmsprache)
        Programmkonfiguration.append(Status_Debug)
        Programmkonfiguration.append(Status_Vollbild)
        Programmkonfiguration.append(Max_FPS)
        Programmkonfiguration.append(Fenstergroesse)
        Programmkonfiguration.append(Kachelgroesse)
        Programmkonfiguration.append(IP_Adresse)
        Programmkonfiguration.append(Port)
        Programmkonfiguration.append(Paketgroesse)
        Programmkonfiguration.append(Lizenz)
        Programmkonfiguration.append(Herausgeber)

        # Rueckgabewert festlegen
        return Programmkonfiguration
    else:
        # ToDo Fehlermeldung: Die Datei: __ProgKonf__.ini konnte nicht gefunden werden.
        print ('Fehlermeldung: Die Datei: __ProgKonf__.ini konnte nicht gefunden werden.')

        # ToDo AutoRepairTool

        # Rueckgabewert festlegen
        return None