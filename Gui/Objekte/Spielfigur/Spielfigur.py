# Import - Modul: pygame
import pygame

# Import - Modul: math
import math

class Spielfigur(pygame.sprite.Sprite):
    def __init__(self, Spielclient, Position_X, Position_Y):
        # Gruppe festlegen
        self.Gruppe = Spielclient.Gruppe_Objekte

        # Spielfigur festlegen
        pygame.sprite.Sprite.__init__(self, self.Gruppe)

        # Gruppe - Layer festelgen
        self.Gruppe.change_layer(self, 2)

        # Spielclient festlegen
        self.Spielclient = Spielclient

        # Spielfigur - Textur festlegen
        self.Spielfigur_Textur = self.Spielclient.Spielfigur_Textur.festlegen_bild(0, 0)

        # Spielfigur - Objekt festlegen
        self.Spielfigur_Objekt = self.Spielfigur_Textur.get_rect()

        # Spielfigur - Eigenschaften festlegen
        self.Spielfigur_Geschwindigkeit = 100

        # Vektor festlegen
        self.Vektor = pygame.math.Vector2

        # Spielfigur - Ausrichtung festlegen
        self.Spielfigur_Ausrichtung = self.Vektor(0, 0)

        # Spielfigur - Position festlegen
        self.Spielfigur_Position = self.Vektor(Position_X , Position_Y) * Spielclient.Programmkonfiguration[8]

        # Spielfigur - Animation - Index festlegen
        self.Spielfigur_Animation_Index = 0

        # Spielfigur - Animation - Zeit festlegen
        self.Spielfigur_Animation_Zeit = 0.2

        # Spielfigur - Animation - Aktuelle - Zeit festlegen
        self.Spielfigur_Animation_Aktuelle_Zeit = 0

    def festlegen_animationen(self, ID_Richtung):
        # Liste - Bewegung festlegen
        Liste_Bewegung = {0: self.Spielclient.Spielfigur_Textur.festlegen_bilder(((0 * 64, 10 * 64), (1 * 64, 10 * 64), (2 * 64, 10 * 64), (3 * 64, 10 * 64), (4 * 64, 10 * 64), (5 * 64, 10 * 64), (6 * 64, 10 * 64), (7 * 64, 10 * 64), (8 * 64, 10 * 64))),
                          1: self.Spielclient.Spielfigur_Textur.festlegen_bilder(((0 * 64, 9 * 64), (1 * 64, 9 * 64), (2 * 64, 9 * 64), (3 * 64, 9 * 64), (4 * 64, 9 * 64), (5 * 64, 9 * 64), (6 * 64, 9 * 64), (7 * 64, 9 * 64), (8 * 64, 9 * 64))),
                          2: self.Spielclient.Spielfigur_Textur.festlegen_bilder(((0 * 64, 11 * 64), (1 * 64, 11 * 64), (2 * 64, 11 * 64), (3 * 64, 11 * 64), (4 * 64, 11 * 64), (5 * 64, 11 * 64), (6 * 64, 11 * 64), (7 * 64, 11 * 64), (8 * 64, 11 * 64))),
                          3: self.Spielclient.Spielfigur_Textur.festlegen_bilder(((0 * 64, 8 * 64), (1 * 64, 8 * 64), (2 * 64, 8 * 64), (3 * 64, 8 * 64), (4 * 64, 8 * 64), (5 * 64, 8 * 64), (6 * 64, 8 * 64), (7 * 64, 8 * 64), (8 * 64, 8 * 64))),
                          99: self.Spielclient.Spielfigur_Textur.festlegen_bilder(((0 * 64, 20 * 64), (1 * 64, 20 * 64), (2 * 64, 20 * 64), (3 * 64, 20 * 64), (4 * 64, 20 * 64), (5 * 64, 20 * 64), (4 * 64, 20 * 64), (3 * 64, 20 * 64), (2 * 64, 20 * 64), (1 * 64, 20 * 64)))}

        # Rueckgabewert festlegen
        return Liste_Bewegung[ID_Richtung]

    def festlegen_richtung(self):
        # Pruefen, in welche Richtung die Spielfigur sich bewegt
        if (abs(self.Spielfigur_Ausrichtung.x) > abs(self.Spielfigur_Ausrichtung.y)):
            # Pruefen, ob die Spielfigur nach links oder rechts sich bewegt
            if (self.Spielfigur_Ausrichtung.x >= 0):
                # ID - Richtung festlegen
                ID_Richtung = 2
            else:
                # ID - Richtung festlegen
                ID_Richtung = 1
        elif (abs(self.Spielfigur_Ausrichtung.y) > abs(self.Spielfigur_Ausrichtung.x)):
            # Pruefen, ob die Spielfigur nach oben oder unten sich bewegt
            if (self.Spielfigur_Ausrichtung.y >= 0):
                # ID - Richtung festlegen
                ID_Richtung = 0
            else:
                # ID - Richtung festlegen
                ID_Richtung = 3
        else:
            # ID - Richtung festlegen
            ID_Richtung = 99

        # Rueckgabewert festlegen
        return ID_Richtung

    def festlegen_kollision(self, Objekt):
        if ((Objekt.x <= self.Spielfigur_Objekt.x <= Objekt.x + Objekt.width) and (Objekt.y <= self.Spielfigur_Objekt.y <= Objekt.y + Objekt.height)):
            # Rueckgabewert festlegen
            return True
        elif ((Objekt.x <= self.Spielfigur_Objekt.x + self.Spielfigur_Objekt.width <= Objekt.x + Objekt.width) and (Objekt.y <= self.Spielfigur_Objekt.y <= Objekt.y + Objekt.height)):
            # Rueckgabewert festlegen
            return True
        elif ((Objekt.x <= self.Spielfigur_Objekt.x <= Objekt.x + Objekt.width) and (Objekt.y <= self.Spielfigur_Objekt.y + self.Spielfigur_Objekt.height <= Objekt.y + Objekt.height)):
            # Rueckgabewert festlegen
            return True
        elif ((Objekt.x <= self.Spielfigur_Objekt.x + self.Spielfigur_Objekt.width <= Objekt.x + Objekt.width) and (Objekt.y <= self.Spielfigur_Objekt.y + self.Spielfigur_Objekt.height <= Objekt.y + Objekt.height)):
            # Rueckgabewert festlegen
            return True
        else:
            # Rueckgabewert festlegen
            return False

    def festlegen_bewegung(self, Sprite):
        # Objekt festlegen
        for Variable in list(vars(Sprite)):
            # Pruefen, ob es sich hier um das Objekt handelt
            if ('Objekt' in Variable):
                # Objekt festlegen
                Objekt = getattr(Sprite, Variable)

        # Pruefen, ob Spielfigur mit Sprite kollidiert
        if (self.festlegen_kollision(Objekt)):
            if (Objekt != self):
                if (math.hypot((self.Spielfigur_Objekt.centerx - Objekt.centerx), (self.Spielfigur_Objekt.centery - Objekt.centery)) <= self.Spielclient.Programmkonfiguration[8]):
                    # Pruefen, ob sich Spielfigur unterhalb des Objektes befindet
                    if (self.Spielfigur_Objekt.centery >= Objekt.centery):
                        self.Gruppe.change_layer(Sprite, 1)
                    else:
                        self.Gruppe.change_layer(Sprite, 2)
        else:
            self.Gruppe.change_layer(Sprite, 2)

    def steuerung(self):
        # Spielfigur - Ausrichtung festlegen
        self.Spielfigur_Ausrichtung = self.Vektor(0, 0)

        # Spielfigur - Bewegung: Horizontal
        if ((self.Spielclient.Spielsteuerung.get_axis(0) < (-1) * self.Spielclient.Programmkonfiguration[9]) or (self.Spielclient.Spielsteuerung.get_axis(0) > self.Spielclient.Programmkonfiguration[9])):
            self.Spielfigur_Ausrichtung.x = self.Spielclient.Spielsteuerung.get_axis(0) * self.Spielfigur_Geschwindigkeit

        # Spielfigur - Bewegung: Vertikal
        if ((self.Spielclient.Spielsteuerung.get_axis(1) < (-1) * self.Spielclient.Programmkonfiguration[9]) or (self.Spielclient.Spielsteuerung.get_axis(1) > self.Spielclient.Programmkonfiguration[9])):
            self.Spielfigur_Ausrichtung.y = self.Spielclient.Spielsteuerung.get_axis(1) * self.Spielfigur_Geschwindigkeit

        # Pruefen, ob die Spielfigur rennen soll
        if (self.Spielclient.Spielsteuerung.get_axis(2) > 0):
            # Spielfigur - Geschwindigkeit festlegen
            self.Spielfigur_Geschwindigkeit = 300

            # Spielfigur - Animation - Zeit festlegen
            self.Spielfigur_Animation_Zeit = 0.07
        elif (self.Spielclient.Spielsteuerung.get_axis(2) <= 0):
            # Spielfigur - Geschwindigkeit festlegen
            self.Spielfigur_Geschwindigkeit = 100

            # Spielfigur - Animation - Zeit festlegen
            self.Spielfigur_Animation_Zeit = 0.2

    def animation(self, dt):
        # ID - Richtung festlegen
        ID_Richtung = self.festlegen_richtung()

        # Liste - Animation festlegen
        Liste_Animation = self.festlegen_animationen(ID_Richtung)

        # Spielfigur - Animation - Aktuelle - Zeit festlegen
        self.Spielfigur_Animation_Aktuelle_Zeit += dt

        # Pruefen, ob die Animation abgespielt werden muss
        if (self.Spielfigur_Animation_Aktuelle_Zeit >= self.Spielfigur_Animation_Zeit):
            # Spielfigur - Animation - Aktuelle - Zeit festlegen
            self.Spielfigur_Animation_Aktuelle_Zeit = 0

            # Spielfigur - Texturindex festlegen
            self.Spielfigur_Animation_Index = (self.Spielfigur_Animation_Index + 1) % len(Liste_Animation)

            # Spielfigur - Textur festlegen
            self.Spielfigur_Textur = Liste_Animation[self.Spielfigur_Animation_Index]

        # Pruefen, ob die Animation vollstaendig abgespielt wurde
        if (self.Spielfigur_Animation_Index >= len(Liste_Animation)):
            # Spielfigur - Texturindex festlegen
            self.Spielfigur_Animation_Index = 0

        # Spielfigur - Textur festlegen
        self.Spielfigur_Textur = Liste_Animation[self.Spielfigur_Animation_Index]

    def update(self):
        # Spielfigur - Steuerung festlegen
        self.steuerung()

        # Spielfigur - Animation festlegen
        self.animation(self.Spielclient.Programmzeit)

        # Pruefen, ob Spieler kollidiert
        for Sprite in self.Gruppe:
            # Pruefen, ob das Sprite die Spielfigur ist
            if (Sprite != self):
                # Kollision festlegen
                self.festlegen_bewegung(Sprite)

        # Spielfigur - Position festlegen
        self.Spielfigur_Position += self.Spielfigur_Ausrichtung * self.Spielclient.Programmzeit

        # Spielfigur - Objekt - Position - X festlegen
        self.Spielfigur_Objekt.x = self.Spielfigur_Position.x

        # Spielfigur - Objekt - Position - Y festlegen
        self.Spielfigur_Objekt.y = self.Spielfigur_Position.y