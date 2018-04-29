# Import - Modul: pygame
import pygame

# Import - Modul: os
import os

# Import - Modul: Variablen
from Konfiguration import Variablen

# Import - Modul: programmkonfiguration_laden
from Engine.System.Programmkonfiguration import programmkonfiguration_laden

# Import - Modul: sprachmodul_laden
from Engine.System.Sprachmodul import sprachmodul_laden

class Spielclient_Hauptfenster:
    def __init__(self):
        # Programmkonfiguration festlegen
        self.Programmkonfiguration = programmkonfiguration_laden()

        # Sprachmodul festlegen
        self.Sprachmodul = sprachmodul_laden(self.Programmkonfiguration[1])

        # Clientfenster festlegen
        if (self.Programmkonfiguration[3]):
            self.Clientfenster = pygame.display.set_mode(self.Programmkonfiguration[5], pygame.FULLSCREEN)
        else:
            self.Clientfenster = pygame.display.set_mode(self.Programmkonfiguration[5])

        # Programmuhr festlegen
        self.Programmuhr = pygame.time.Clock()

        # Spielclient - Socket festlegen
        Status_Sockets = self.erstellen_socket()

        # Spielclient - Gruppen festlegen
        Status_Gruppen = self.erstellen_gruppen()

        # Spielclient - Objekte festlegen
        Status_Objekte = self.erstellen_objekte()

        # Status - Spielclient festlegen
        self.Status_Spielclient = self.festlegen_status(Status_Sockets, Status_Gruppen, Status_Objekte)

    def laden_daten(self):
        # Pfad - Texturen festlegen
        Pfad_Texturen = self.festlegen_pfad(0)

        # Pfad - Szenen festlegen
        Pfad_Szenen = self.festlegen_pfad(1)

        # Spielsteuerung festlegen
        self.Spielsteuerung = self.festlegen_steuerung()

        # Daten - Spielfigur festlegen
        self.Daten_Spielfigur = None

        # Textur - Spielfigur festlegen
        self.Textur_Spielfigur = pygame.image.load(os.path.join(Pfad_Texturen, 'Textur_Spielfigur..png'))

    def erstellen_socket(self):
        # TODO DEBUG: Rueckgabewert True
        return True

    def erstellen_gruppen(self):
        # TODO DEBUG: Rueckgabewert True
        return True

    def erstellen_objekte(self):
        # TODO DEBUG: Rueckgabewert True
        return True

    def festlegen_pfad(self, ID_Pfad):
        # Pfad festlegen
        Pfad = {0: 'Texturen',
                1: 'Szenen'}

        # Pruefen, ob der Pfad verfuegbar ist
        if (os.path.exists(os.path.join(Variablen.Pfad_Grundverzeichnis, 'Dateien', Pfad[ID_Pfad]))):
            # Rueckgabewert festlegen
            return os.path.join(Variablen.Pfad_Grundverzeichnis, 'Dateien', Pfad[ID_Pfad])
        else:
            # ToDo Fehlermeldung: Der angegebene Pfad konnte nicht gefunden werden!
            print('Fehlermeldung: Der angegebene Pfad konnte nicht gefunden werden!')

            # ToDo AutoRepairTool starten!

            # Rueckgabewert festlegen
            return None

    def festlegen_status(self, Status_Sockets, Status_Gruppen, Status_Objekte):
        # Pruefen, ob Spielclient mit allen Eigenschaften gestartet werden konnte
        if ((Status_Sockets) and (Status_Gruppen) and (Status_Objekte)):
            # Rueckgabewert festlegen
            return True
        else:
            # Rueckgabewert festlegen
            return False

    def festlegen_steuerung(self):
        pass

    def programmschleife(self):
        pass

    def events(self):
        pass

    def beenden(self):
        pass

    def update(self):
        pass

    def zeichnen(self):
        pass