# Import - Modul: pygame
import pygame

class Spritesheet(object):
    def __init__(self, Dateiname, Bildgroesse):
        # SpriteSheet - Eigenschaften festlegen
        self.Breite_Bild = Bildgroesse[0]
        self.Hoehe_Bild = Bildgroesse[1]

        # Versuch: SpriteSheet zu laden
        try:
            # SpriteSheet festlegen
            self.SpriteSheet = pygame.image.load(Dateiname)
        except:
            # ToDo Fehlermeldung: Das SpriteSheet konnte nicht geladen werden!
            print ('Das SpriteSheet konnte nicht geladen werden!')

    def festlegen_bild(self, Position_X, Position_Y):
        # Bildbereich festlegen
        Bildbereich = pygame.Rect((Position_X, Position_Y, self.Breite_Bild, self.Hoehe_Bild))

        # Bild festlegen
        Bild = pygame.Surface(Bildbereich.size, pygame.SRCALPHA)

        # Bild zeichnen
        Bild.blit(self.SpriteSheet, (0, 0), Bildbereich)

        # Rueckgabewert festlegen
        return Bild

    def festlegen_bilder(self, Liste_Bereich):
        # Rueckgabewert festlegen
        return [self.festlegen_bild(Bildbereich[0], Bildbereich[1]) for Bildbereich in Liste_Bereich]