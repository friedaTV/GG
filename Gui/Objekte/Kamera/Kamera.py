# Import - Modul: pygame
import pygame

class Kamera:
    def __init__(self, Breite, Hoehe):
        # Kamera - Objekt festlegen
        self.Kamera_Objekt = pygame.Rect(0, 0, Breite, Hoehe)

        # Kamera - Eigenschaften festlegen
        self.Breite = Breite
        self.Hoehe = Hoehe

    def binden_objekt(self, Objekt):
        # Variablen pruefen
        for Variable in list(vars(Objekt)):
            # Pruefen, ob es sich hier um das Objekt handelt
            if ('Objekt' in Variable):
                # Objekt - Objekt festlegen
                Objekt_Objekt = getattr(Objekt, Variable)

        # Rueckgabewert festlegen
        return Objekt_Objekt.move(self.Kamera_Objekt.topleft)

    def binden_spielwelt(self, Spielwelt):
        # Rueckgabewert festlegen
        return Spielwelt.move(self.Kamera_Objekt.topleft)

    def update(self, Objekt, Fensterbreite, Fensterhoehe):
        # Variablen pruefen
        for Variable in list(vars(Objekt)):
            # Pruefen, ob es sich hier um das Objekt handelt
            if ('Objekt' in Variable):
                # Objekt - Objekt festlegen
                Objekt_Objekt = getattr(Objekt, Variable)

        # Offset - X festlegen
        Offset_X = (-1) * Objekt_Objekt.centerx + int(Fensterbreite / 2)

        # Offset - Y festlegen
        Offset_Y = (-1) * Objekt_Objekt.centery + int(Fensterhoehe / 2)

        # Kamera - Bewegung festlegen
        X = min(0, Offset_X)
        Y = min(0, Offset_Y)
        X = max((-1) * (self.Breite - Fensterbreite), X)
        Y = max((-1) * (self.Hoehe - Fensterhoehe), Y)

        # Kamera - Objekt festlegen
        self.Kamera_Objekt = pygame.Rect(X, Y, self.Breite, self.Hoehe)