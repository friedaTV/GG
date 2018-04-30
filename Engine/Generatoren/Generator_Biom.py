# Import - Modul: random
import random

# Import - Modul: numpy
import numpy

class Biom:
    def __init__(self, Seed_Planet, ID_Biom, Liste_Startecken):
        # Random - Seed festlegen
        random.seed(Seed_Planet)

        # Biomgroesse festlegen
        self.Biomgroesse = 1024 + 1

        # Hilfsgroesse festlegen
        self.Hilfsgroesse = self.Biomgroesse - 1

        # Liste - Quadranten festlegen
        self.Liste_Quadranten = numpy.full((self.Biomgroesse, self.Biomgroesse), None)

        # Startpunkte festlegen
        self.festlegen_startpunkte(Liste_Startecken)

        # Quadranten festlegen
        self.festlegen_quadrant(self.Hilfsgroesse)

    def festlegen_startpunkte(self, Liste_Startecken):
        # Ecke - Linksoben festlegen
        self.Liste_Quadranten[0][0] = Liste_Startecken[0]

        # Ecke - Rechtsoben festlegen
        self.Liste_Quadranten[self.Hilfsgroesse][0] = Liste_Startecken[1]

        # Ecke - Rechtsunten festlegen
        self.Liste_Quadranten[self.Hilfsgroesse][self.Hilfsgroesse] = Liste_Startecken[2]

        # Ecke - Linksunten festlegen
        self.Liste_Quadranten[0][self.Hilfsgroesse] = Liste_Startecken[3]

    def festlegen_id(self, Liste_Eckpunkte):
        # Liste - Vorzeichen festlegen
        Liste_Vorzeichen = [-1, 1]

        # ID festlegen
        ID = sum(Liste_Eckpunkte) / len(Liste_Eckpunkte) + (Liste_Vorzeichen[random.randint(0, 1)]) * random.uniform(0.1, 0.5)

        # Pruefen, ob 0 <= ID <= 1
        if (ID < 0):
            # ID festlegen
            ID = 0
        elif (ID > 1):
            # ID festlegen
            ID = 1
        else:
            # ID festlegen
            ID = ID

        # Rueckgabewert festlegen
        return ID

    def festlegen_eigenschaften(self, Seed_Planet):
        pass

    def festlegen_quadrant(self, Groesse):
        # Halbschritt festlegen
        Halbschritt = int(Groesse / 2)

        # Pruefen, ob das Biom fertig generiert ist
        if (Halbschritt < 1):
            return

        # Vierecke berechnen
        for Position_Y in range(Halbschritt, self.Hilfsgroesse, Groesse):
            for Position_X in range(Halbschritt, self.Hilfsgroesse, Groesse):
                # Viereck festlegen
                self.viereck(Position_X, Position_Y, Halbschritt)

        # Diamanten berechnen
        for Position_Y in range(0, self.Hilfsgroesse + 1, Halbschritt):
            for Position_X in range((Position_Y + Halbschritt) % Groesse, self.Hilfsgroesse + 1, Groesse):
                # Diamant festlegen
                self.diamant(Position_X, Position_Y, Halbschritt)

        # Biom berechnen
        self.festlegen_quadrant(int(Groesse / 2))

    def viereck(self, Position_X, Position_Y, Groesse):
        # Ecke - Linksoben festlegen
        Ecke_Linksoben = self.Liste_Quadranten[Position_X - Groesse][Position_Y - Groesse]

        # Ecke - Rechtsoben festlegen
        Ecke_Rechtsoben = self.Liste_Quadranten[Position_X + Groesse][Position_Y - Groesse]

        # Ecke - Linksunten festlegen
        Ecke_Linksunten = self.Liste_Quadranten[Position_X + Groesse][Position_Y + Groesse]

        # Ecke - Rechtsunten festlegen
        Ecke_Rechtsunten = self.Liste_Quadranten[Position_X - Groesse][Position_Y + Groesse]

        # ID - Quadrant festlegen
        ID_Quadrant = self.festlegen_id((Ecke_Linksoben, Ecke_Rechtsoben, Ecke_Linksunten, Ecke_Rechtsunten))

        # Liste - Quadranten festlegen
        self.Liste_Quadranten[Position_X][Position_Y] = ID_Quadrant

    def diamant(self, Position_X, Position_Y, Groesse):
        # Liste - Eckpunkte festlegen
        Liste_Eckpunkte = []

        # Pruefen, ob sich der zu berechnende Punkt an der Biomgrenze befindet
        # Norden
        if (Position_Y == 0):
            # Ecke - Rechts festlegen
            Liste_Eckpunkte.append(self.Liste_Quadranten[Position_X + Groesse][Position_Y])

            # Ecke - Unten festlegen
            Liste_Eckpunkte.append(self.Liste_Quadranten[Position_X][Position_Y + Groesse])

            # Ecke - Links festlegen
            Liste_Eckpunkte.append(self.Liste_Quadranten[Position_X - Groesse][Position_Y])
        # Osten
        elif (Position_X == self.Hilfsgroesse):
            # Ecke - Top festlegen
            Liste_Eckpunkte.append(self.Liste_Quadranten[Position_X][Position_Y - Groesse])

            # Ecke - Unten festlegen
            Liste_Eckpunkte.append(self.Liste_Quadranten[Position_X][Position_Y + Groesse])

            # Ecke - Links festlegen
            Liste_Eckpunkte.append(self.Liste_Quadranten[Position_X - Groesse][Position_Y])
        # Sueden
        elif (Position_Y == self.Hilfsgroesse):
            # Ecke - Top festlegen
            Liste_Eckpunkte.append(self.Liste_Quadranten[Position_X][Position_Y - Groesse])

            # Ecke - Rechts festlegen
            Liste_Eckpunkte.append(self.Liste_Quadranten[Position_X + Groesse][Position_Y])

            # Ecke - Links festlegen
            Liste_Eckpunkte.append(self.Liste_Quadranten[Position_X][Position_Y - Groesse])
        # Westen
        elif (Position_X == 0):
            # Ecke - Top festlegen
            Liste_Eckpunkte.append(self.Liste_Quadranten[Position_X][Position_Y - Groesse])

            # Ecke - Rechts festlegen
            Liste_Eckpunkte.append(self.Liste_Quadranten[Position_X + Groesse][Position_Y])

            # Ecke - Unten festlegen
            Liste_Eckpunkte.append(self.Liste_Quadranten[Position_X][Position_Y + Groesse])
        else:
            # Ecke - Top festlegen
            Liste_Eckpunkte.append(self.Liste_Quadranten[Position_X][Position_Y - Groesse])

            # Ecke - Rechts festlegen
            Liste_Eckpunkte.append(self.Liste_Quadranten[Position_X + Groesse][Position_Y])

            # Ecke - Unten festlegen
            Liste_Eckpunkte.append(self.Liste_Quadranten[Position_X][Position_Y + Groesse])

            # Ecke - Links festlegen
            Liste_Eckpunkte.append(self.Liste_Quadranten[Position_X - Groesse][Position_Y])

        # ID - Quadrant festlegen
        ID_Quadrant = self.festlegen_id(Liste_Eckpunkte)

        # Liste - Quadranten festlegen
        self.Liste_Quadranten[Position_X][Position_Y] = ID_Quadrant