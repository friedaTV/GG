# Import - Modul: pygame
import pygame

class Spielfigur(pygame.sprite.Sprite):
    def __init__(self, Spielclient, Position_X, Position_Y):
        # Gruppe festlegen
        self.Gruppe = Spielclient.Gruppe_Objekte

        # Spielfigur festlegen
        pygame.sprite.Sprite.__init__(self, self.Gruppe)

        # Spielclient festlegen
        self.Spielclient = Spielclient

        # Spielfigur - Textur festlegen
        self.Spielfigur_Textur = self.Spielclient.Textur_Spielfigur

        # Spielfigur - Objekt festlegen
        self.Spielfigur_Objekt = self.Spielfigur_Textur.get_rect()

        # Spielfigur - Eigenschaften festlegen
        self.Spielfigur_Geschwindigkeit = 300

        # Vektor festlegen
        self.Vektor = pygame.math.Vector2

        # Spielfigur - Ausrichtung festlegen
        self.Spielfigur_Ausrichtung = self.Vektor(0, 0)

        # Spielfigur - Position festlegen
        self.Spielfigur_Position = self.Vektor(Position_X, Position_Y) * Spielclient.Programmkonfiguration[8]

    def steuerung(self):
        # Spielfigur - Ausrichtung festlegen
        self.Spielfigur_Ausrichtung = self.Vektor(0, 0)

        # Spielfigur - Bewegung: Horizontal
        if ((self.Spielclient.Spielsteuerung.get_axis(0) < (-1) * self.Spielclient.Programmkonfiguration[9]) or (self.Spielclient.Spielsteuerung.get_axis(0) > self.Spielclient.Programmkonfiguration[9])):
            self.Spielfigur_Ausrichtung.x = self.Spielclient.Spielsteuerung.get_axis(0) * self.Spielfigur_Geschwindigkeit

        # Spielfigur - Bewegung: Vertikal
        if ((self.Spielclient.Spielsteuerung.get_axis(1) < (-1) * self.Spielclient.Programmkonfiguration[9]) or (self.Spielclient.Spielsteuerung.get_axis(1) > self.Spielclient.Programmkonfiguration[9])):
            self.Spielfigur_Ausrichtung.y = self.Spielclient.Spielsteuerung.get_axis(1) * self.Spielfigur_Geschwindigkeit

    def update(self):
        # Spielfigur - Steuerung festlegen
        self.steuerung()

        # Spielfigur - Position festlegen
        self.Spielfigur_Position += self.Spielfigur_Ausrichtung * self.Spielclient.Programmzeit

        # Spielfigur - Objekt - Position - X festlegen
        self.Spielfigur_Objekt.x = self.Spielfigur_Position.x

        # Spielfigur - Objekt - Position - Y festlegen
        self.Spielfigur_Objekt.y = self.Spielfigur_Position.y