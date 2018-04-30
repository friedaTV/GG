# Import - Modul: pygame
import pygame

class Spielwelt:
    def __init__(self, Datensatz):
        # Spielwelt - Eigenschaften festlegen
        self.Breite = Datensatz.Planet_Eigenschaften[0] * Datensatz.Liste_Biome[0][0].Biomgroesse * 64
        self.Hoehe = Datensatz.Planet_Eigenschaften[1] * Datensatz.Liste_Biome[0][0].Biomgroesse * 64

        # Spielwelt - Textur - Debug festlegen
        self.Spielwelt_Textur_Debug = pygame.image.load('E:\Python\GG\Dateien\Texturen\Textur_Debug.png')

        # Spielwelt - Textur festlegen
        self.Spielwelt_Textur = self.karte_erstellen()

        # Spielwelt - Objekt festlegen
        self.Spielwelt_Objekt = self.Spielwelt_Textur.get_rect()

    def zeichnen(self, Objekt):
        for Position_Y in range(self.Hoehe):
            for Position_X in range(self.Breite):
                Objekt.blit(self.Spielwelt_Textur_Debug, (Position_X * 64, Position_Y * 64))

    def karte_erstellen(self):
        # Spielwelt - Objekt festlegen
        Spielwelt_Objekt = pygame.Surface((self.Breite, self.Hoehe))

        # Spielwelt zeichnen
        self.zeichnen(Spielwelt_Objekt)

        # Rueckgabewert festlegen
        return Spielwelt_Objekt