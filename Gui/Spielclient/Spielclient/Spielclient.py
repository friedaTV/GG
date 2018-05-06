# Import - Modul: pygame
import pygame

# Import - Modul: os
import os

# Import - Modul: sys
import sys

# Import - Modul: random
import random

# Import - Modul: Variablen
from Konfiguration import Variablen

# Import - Modul: programmkonfiguration_laden
from Engine.System.Programmkonfiguration import programmkonfiguration_laden

# Import - Modul: sprachmodul_laden
from Engine.System.Sprachmodul import sprachmodul_laden

# Import - Modul: Spielfigur
from Gui.Objekte.Spielfigur.Spielfigur import Spielfigur

# Import - Modul: Baum
from Gui.Objekte.Vegetation.Baum import Baum

# Import - Modul: Kamera
from Gui.Objekte.Kamera.Kamera import Kamera

# Import - Modul: Spielwelt
from Gui.Objekte.Spielwelt.Spielwelt import Spielwelt

# Import - Modul: Spritesheet
from Engine.Grafik.Spritesheet import Spritesheet

class Spielclient:
    def __init__(self):
        # Programmkonfiguration festlegen
        self.Programmkonfiguration = programmkonfiguration_laden()

        # Sprachmodul festlegen
        self.Sprachmodul = sprachmodul_laden(self.Programmkonfiguration[1])

        # Clientfenster festlegen
        if (self.Programmkonfiguration[3]):
            self.Clientfenster = pygame.display.set_mode(self.Programmkonfiguration[7], pygame.FULLSCREEN)
        else:
            self.Clientfenster = pygame.display.set_mode(self.Programmkonfiguration[7])

        # Clientfenster - Titel festlegen
        pygame.display.set_caption(self.Programmkonfiguration[0] + ' ' + self.Programmkonfiguration[1] + ' ' + self.Programmkonfiguration[2])

        # Programmuhr festlegen
        self.Programmuhr = pygame.time.Clock()

        # Spielclient - Texturen festlegen
        self.laden_texturen()

        # Spielclient - Daten festlegen
        self.laden_daten()

        # Spielclient - Socket festlegen
        Status_Sockets = self.erstellen_socket()

        # Spielclient - Gruppen festlegen
        Status_Gruppen = self.erstellen_gruppen()

        # Spielclient - Objekte festlegen
        Status_Objekte = self.erstellen_objekte()

        # Status - Spielclient festlegen
        self.Status_Spielclient = self.festlegen_status(Status_Sockets, Status_Gruppen, Status_Objekte)

    def laden_texturen(self):
        # Pfad - Texturen festlegen
        Pfad_Texturen = self.festlegen_pfad(0)

        # Spielfigur - Textur festlegen
        self.Spielfigur_Textur = Spritesheet(os.path.join(Pfad_Texturen, 'Spielfigur_SpriteSheet.png'), (64, 64))

        # Baum - Textur festlegen
        self.Baum_Textur = Spritesheet(os.path.join(Pfad_Texturen, 'Baum_SpriteSheet.png'), (64, 96))

    def laden_daten(self):
        # Spielsteuerung und Status - Spielsteuerung festlegen
        self.Spielsteuerung, self.Status_Spielsteuerung = self.festlegen_steuerung()

        # Daten - Spielfigur festlegen
        self.Spielfigur_Daten = None

    def erstellen_socket(self):
        # TODO DEBUG: Rueckgabewert True
        return True

    def erstellen_gruppen(self):
        # Gruppe - Objekte festlegen
        self.Gruppe_Objekte = pygame.sprite.Group()

        # Gruppe - Vegetation festlegen
        self.Gruppe_Vegetation = pygame.sprite.Group()

        # Rueckgabewert festlegen
        return True

    def erstellen_objekte(self):
        # Objekt - Spielfigur festlegen
        self.Objekt_Spielfigur = Spielfigur(self, 1, 1)

        # Objekt - Baum festlegen
        self.Objekt_Baum = Baum(self, random.randint(0, 15), random.randint(0, 15))

        # Objekt - Spielwelt festlegen
        self.Objekt_Spielwelt = Spielwelt()

        # Objekt - Kamera festlegen
        self.Objekt_Kamera = Kamera(self.Objekt_Spielwelt.Spielwelt_Breite, self.Objekt_Spielwelt.Spielwelt_Hoehe)

        # Rueckgabewert festlegen
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

            # Status - Spielsteuerung festlegen
            Status_Spielsteuerung = True
        except:
            # Spielkontroller festlegen
            Spielkontroller = None

            # Status - Spielsteuerung festlegen
            Status_Spielsteuerung = False

        # Rueckgabewert festlegen
        return Spielkontroller, Status_Spielsteuerung

    def programmschleife(self):
        # Programmschleife festlegen
        while (self.Status_Spielclient):
            # Programmzeit festlegen
            self.Programmzeit = self.Programmuhr.tick(self.Programmkonfiguration[6]) / 1000

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
        # Gruppe - Objekte updaten
        self.Gruppe_Objekte.update()

        # Gruppe - Vegetations updaten
        self.Gruppe_Vegetation.update()

        # Objekt - Kamera updaten
        self.Objekt_Kamera.update(self.Objekt_Spielfigur, self.Programmkonfiguration[7][0], self.Programmkonfiguration[7][1])

    def zeichnen(self):
        # Spielwelt zeichnen
        self.Clientfenster.blit(self.Objekt_Spielwelt.Spielwelt_Textur, self.Objekt_Kamera.binden_spielwelt(self.Objekt_Spielwelt.Spielwelt_Objekt))

        # Gruppe - Objekte zeichnen
        for Sprite in self.Gruppe_Objekte:
            # Objekt - Textur festlegen
            for Variable in list(vars(Sprite)):
                # Pruefen, ob es sich hier um das Objekt handelt
                if ('Textur' in Variable):
                    # Objekt - Textur festlegen
                    Objekt_Textur = getattr(Sprite, Variable)

            self.Clientfenster.blit(Objekt_Textur, self.Objekt_Kamera.binden_objekt(Sprite))

        # Gruppe - Vegetation zeichnen
        for Sprite in self.Gruppe_Vegetation:
            # Objekt - Textur festlegen
            for Variable in list(vars(Sprite)):
                # Pruefen, ob es sich hier um das Objekt handelt
                if ('Textur' in Variable):
                    # Objekt - Textur festlegen
                    Objekt_Textur = getattr(Sprite, Variable)

            self.Clientfenster.blit(Objekt_Textur, self.Objekt_Kamera.binden_objekt(Sprite))

        # PyGame aktualisieren
        pygame.display.flip()