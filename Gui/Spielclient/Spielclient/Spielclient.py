# Import - Modul: pygame
import pygame

# Import - Modul: os
import os

# Import - Modul: sys
import sys

# Import - Modul: Variablen
from Konfiguration import Variablen

# Import - Modul: programmkonfiguration_laden
from Engine.System.Programmkonfiguration import programmkonfiguration_laden

# Import - Modul: sprachmodul_laden
from Engine.System.Sprachmodul import sprachmodul_laden

class Spielclient:
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

        # Spielclient - Daten festlegen
        self.laden_daten()

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
        self.Textur_Spielfigur = None

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
        # Versuch: Spielkontroller festzulegen
        try:
            # Spielkontroller festlegen
            Spielkontroller = pygame.joystick.Joystick(0)

            # Spielkontroller initialisieren
            Spielkontroller.init()
        except:
            # Spielkontroller festlegen
            Spielkontroller = None

        # Rueckgabewert festlegen
        return Spielkontroller

    def programmschleife(self):
        # Programmschleife festlegen
        while (self.Status_Spielclient):
            # Programmzeit festlegen
            self.Programmzeite = self.Programmuhr.tick(self.Programmkonfiguration[4]) / 1000

            # Spielclient - Events festlegen
            self.events()

            # Spielclient - Update festlegen
            self.update()

            # Spielclient - Zeichnen
            self.zeichnen()

    def events(self):
        for Event in pygame.event.get():
            # Pruefen, ob der Button: Schliessen gedrueckt wurde
            if (Event.type == pygame.QUIT):
                # Spielclient - Beenden
                self.beenden()

            # Pruefen, ob eine Taste auf der Tastatur gedrueckt wurde
            if (Event.type == pygame.KEYDOWN):
                # Pruefen, ob K_ESCAPE gedrueckt wurde
                if (Event.key == pygame.K_ESCAPE):
                    # Spielclient - Beenden
                    self.beenden()

            # Pruefen, ob eine Taste auf dem Spielkontroller gedrueckt wurde
            if (Event.type == pygame.JOYBUTTONDOWN):
                # Pruefen, ob Event.button gleich 6 ist
                if (Event.button == 6):
                    # Spielclient - Beenden
                    self.beenden()

    def beenden(self):
        # PyGame beenden
        pygame.quit()

        # Programm beenden
        sys.exit()

    def update(self):
        pass

    def zeichnen(self):
        pass