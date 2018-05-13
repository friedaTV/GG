# Import - Modul: pygame
import pygame

class Wasser(pygame.sprite.Sprite):
    def __init__(self, Spielclient, Position_X, Position_Y):
        # Gruppe festlegen
        self.Gruppe = Spielclient.Gruppe_Oberflaechen

        # Wasser festlegen
        pygame.sprite.Sprite.__init__(self, self.Gruppe)

        # Spielclient festlegen
        self.Spielclient = Spielclient

        # Wasser - Textur festlegen
        self.Wasser_Textur = self.Spielclient.Wasser_Textur.festlegen_bild(0, 0)

        # Wasser - Objekt festlegen
        self.Wasser_Objekt = self.Wasser_Textur.get_rect()

        # Vektor festlegen
        self.Vektor = pygame.math.Vector2

        # Wasser - Position festlegen
        self.Wasser_Position = self.Vektor(Position_X, Position_Y) * self.Spielclient.Programmkonfiguration[8]

        # Wasser - Index festlegen
        self.Wasser_Index = 0

        # Wasser - Aktuelle - Zeit festlegen
        self.Wasser_Aktuelle_Zeit = 0

        # Wasser - Zeit festlegen
        self.Wasser_Zeit = 0.05

    def animation(self, dt):
        # Wasser - Aktuelle - Zeit festlegen
        self.Wasser_Aktuelle_Zeit += dt

        # Pruefen, ob das Wasser animiert werden muss
        if (self.Wasser_Aktuelle_Zeit >= self.Wasser_Zeit):
            # Wasser - Index festlegen
            self.Wasser_Index += 1

            # Pruefen, ob Wasser - Index groesser gleich 31 ist
            if (self.Wasser_Index >= 31):
                # Wasser - Index festlegen
                self.Wasser_Index = 0

            # Wasser - Textur festlegen
            self.Wasser_Textur = self.Spielclient.Wasser_Textur.festlegen_bild(self.Wasser_Index * self.Wasser_Objekt.width, 0)

            # Wasser - Aktuelle - Zeit festlegen
            self.Wasser_Aktuelle_Zeit = 0

    def update(self):
        # Wasser - Animation festlegen
        self.animation(self.Spielclient.Programmzeit)

        # Wasser - Objekt - Position - X festlegen
        self.Wasser_Objekt.x = self.Wasser_Position.x

        # Wasser - Objekt - Position - Y festlegen
        self.Wasser_Objekt.y = self.Wasser_Position.y