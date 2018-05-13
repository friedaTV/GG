# Import - Modul: pygame
import pygame

class Spielwelt:
    def __init__(self, Spielclient):
        # Spielclient festlegen
        self.Spielclient = Spielclient

        # Spielwelt - Eigenschaften festlegen
        self.Spielwelt_Breite = 32 * self.Spielclient.Programmkonfiguration[8]
        self.Spielwelt_Hoehe = 32 * self.Spielclient.Programmkonfiguration[8]

        # Spielwelt - Textur - Debug festlegen
        self.Spielwelt_Textur_Debug = pygame.image.load('E:\Python\GG\Dateien\Texturen\Textur_Granitplatte.png')

        # Spielwelt - Textur festlegen
        self.Spielwelt_Textur = self.karte_erstellen()

        # Spielwelt - Objekt festlegen
        self.Spielwelt_Objekt = self.Spielwelt_Textur.get_rect()

    def festlegen_cluster(self):
        pass

    def zeichnen(self, Objekt):
        for Position_Y in range(int(self.Spielwelt_Hoehe / self.Spielclient.Programmkonfiguration[8])):
            for Position_X in range(int(self.Spielwelt_Breite / self.Spielclient.Programmkonfiguration[8])):
                Objekt.blit(self.Spielwelt_Textur_Debug, (Position_X * self.Spielclient.Programmkonfiguration[8], Position_Y * self.Spielclient.Programmkonfiguration[8]))

    def karte_erstellen(self):
        # Spielwelt - Objekt festlegen
        Spielwelt_Objekt = pygame.Surface((self.Spielwelt_Breite, self.Spielwelt_Hoehe))

        # Spielwelt zeichnen
        self.zeichnen(Spielwelt_Objekt)

        # Rueckgabewert festlegen
        return Spielwelt_Objekt