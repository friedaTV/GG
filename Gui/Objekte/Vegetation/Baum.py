# Import - Modul: pygame
import pygame

# Import - Modul: numpy
import numpy

class Baum(pygame.sprite.Sprite):
    def __init__(self, Spielclient, Position_X, Position_Y):
        # Gruppe festlegen
        self.Gruppe = Spielclient.Gruppe_Vegetation

        # Baum festlegen
        pygame.sprite.Sprite.__init__(self, self.Gruppe)

        # Spielclient festlegen
        self.Spielclient = Spielclient

        # Baum - Textur festlegen
        self.Baum_Textur = self.Spielclient.Baum_Textur.festlegen_bild(0, 0)

        # Baum - Objekt festlegen
        self.Baum_Objekt = self.Baum_Textur.get_rect()

        # Baum - Eigenschaften festlegen
        self.Status_Baum = True
        self.Baum_Lebenspunkte = 100
        self.Baum_Alter = 0
        self.Baum_Menge_Ressource = 0

        # Vektor festlegen
        self.Vektor = pygame.math.Vector2

        # Baum - Position festlegen
        self.Baum_Position = self.Vektor(Position_X, Position_Y) * Spielclient.Programmkonfiguration[8]

        # Baum - Aktuelle - Zeit festlegen
        self.Baum_Aktuelle_Zeit = 0

        # Baum - Zeit festlegen
        self.Baum_Zeit = 0.4

    def wachsen(self, dt):
        # Pruefen, ob der Baum mehr Lebenspunkte bekommt
        if (numpy.random.randint(0, 99) >= 60):
            # Baum - Lebenspunkte festlegen
            self.Baum_Lebenspunkte += numpy.random.randint(1, 4)

            # Baum - Menge - Ressource festlegen
            self.Baum_Menge_Ressource += numpy.random.randint(0, 1)

        # Baum - Aktuelle - Zeit festlegen
        self.Baum_Aktuelle_Zeit += dt

        # Pruefen, ob der Baum wachsen kann
        if (self.Baum_Aktuelle_Zeit >= self.Baum_Zeit):
            # Baum - Aktuelle - Zeit festlegen
            self.Baum_Aktuelle_Zeit = 0

            # Pruefen, welches Alter der Baum erreicht hat
            if (7 < self.Baum_Alter <= 20):
                # Baum - Textur festlegen
                self.Baum_Textur = self.Spielclient.Baum_Textur.festlegen_bild(64, 0)
            elif (20 < self.Baum_Alter <= 50):
                # Baum - Textur festlegen
                self.Baum_Textur = self.Spielclient.Baum_Textur.festlegen_bild(128, 0)
            elif (50 < self.Baum_Alter <= 120):
                # Baum - Textur festlegen
                self.Baum_Textur = self.Spielclient.Baum_Textur.festlegen_bild(192, 0)
            elif (120 < self.Baum_Alter <= 150):
                # Baum - Textur festlegen
                self.Baum_Textur = self.Spielclient.Baum_Textur.festlegen_bild(256, 0)

            # Baum - Alter festlegen
            self.Baum_Alter += 1

    def sterben(self):
        # Baum loeschen
        self.kill()

    def abbauen(self, Lebenspunkte):
        # Baum - Lebenspunkte festlegen
        self.Baum_Lebenspunkte -= Lebenspunkte

        # Pruefen, ob die Lebenpunkte des Baumes kleiner gleich Null sind
        if (self.Baum_Lebenspunkte <= 0):
            # Status - Baum festlegen
            self.Status_Baum = False

            # Baum - Textur festlegen
            self.Baum_Textur = self.Spielclient.Baum_Textur.festlegen_bild(312, 0)

    def update(self):
        # Pruefen, ob der Baum gefaellt wurde
        if (self.Status_Baum):
            # Pruefen, ob der Baum zu alt ist
            if (self.Baum_Alter >= 150):
                # Baum - sterben
                self.sterben()
            else:
                # Baum - wachsen
                self.wachsen(self.Spielclient.Programmzeit)
        else:
            pass

        # Baum - Objekt - Position - X festlegen
        self.Baum_Objekt.x = self.Baum_Position.x

        # Baum - Objekt - Position - Y festlegen
        self.Baum_Objekt.y = self.Baum_Position.y