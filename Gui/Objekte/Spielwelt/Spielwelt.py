# Import - Modul: pygame
import pygame

class Spielwelt:
    def __init__(self):
        # Spielwelt - Eigenschaften festlegen
        self.Spielwelt_Breite = 1024
        self.Spielwelt_Hoehe = 1024

        # Spielwelt - Textur - Debug festlegen
        self.Spielwelt_Textur_Debug = pygame.image.load('E:\Python\GG\Dateien\Texturen\Textur_Gras_Sommer_Natuerlich.png')

        # Spielwelt - Textur festlegen
        self.Spielwelt_Textur = self.karte_erstellen()

        # Spielwelt - Objekt festlegen
        self.Spielwelt_Objekt = self.Spielwelt_Textur.get_rect()

    def festlegen_cluster(self):
        pass

    def zeichnen(self, Objekt):
        for Position_Y in range(self.Spielwelt_Hoehe):
            for Position_X in range(self.Spielwelt_Breite):
                Objekt.blit(self.Spielwelt_Textur_Debug, (Position_X * 64, Position_Y * 64))

    def karte_erstellen(self):
        # Spielwelt - Objekt festlegen
        Spielwelt_Objekt = pygame.Surface((self.Spielwelt_Breite, self.Spielwelt_Hoehe))

        # Spielwelt zeichnen
        self.zeichnen(Spielwelt_Objekt)

        # Rueckgabewert festlegen
        return Spielwelt_Objekt