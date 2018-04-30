# Import - Modul: random
import random

# Import - Modul: numpy
import numpy

# Import - Modul: Biom
from Engine.Generatoren.Generator_Biom import Biom

class Planet:
    def __init__(self, Seed_Planet):
        # Seed - Planet festlegen
        self.Seed_Planet = Seed_Planet

        # Random - Seed festlegen
        random.seed(self.Seed_Planet)

        # ID - Planet festlegen
        self.ID_Planet = self.festlegen_id()

        # Planet - Eigenschaften festlegen
        self.Planet_Eigenschaften = self.festlegen_eigenschaften(self.ID_Planet)

        # Liste - Biome festlegen
        self.Liste_Biome = numpy.full((self.Planet_Eigenschaften[1], self.Planet_Eigenschaften[0]), None)

        # Liste - Biome fuellen
        self.festlegen_biom((0, 1))

    def festlegen_id(self):
        # Rueckgabewert festlegen
        return random.randint(0, 0)

    def festlegen_liste(self):
        # Liste - Startecken festlegen
        Liste_Startecken = []

        for Position_Y in range(self.Planet_Eigenschaften[1]):
            for Position_X in range(self.Planet_Eigenschaften[0]):
                # Pruefen, welche Startecken berechnet werden sollen
                if (Position_Y == 0):
                    if (Position_X == 0):
                        # Liste - Startecken festlegen
                        Liste_Startecken.append((random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
                    elif (Position_X == self.Planet_Eigenschaften[0] - 1):
                        # Liste - Startecken festlegen
                        Liste_Startecken.append((Liste_Startecken[Position_X - 1][1], Liste_Startecken[0][0], Liste_Startecken[0][3], Liste_Startecken[Position_X - 1][2]))
                    else:
                        # Liste - Startecken festlegen
                        Liste_Startecken.append((Liste_Startecken[Position_X - 1][1], random.uniform(0, 1), random.uniform(0, 1), Liste_Startecken[Position_X - 1][2]))
                elif (0 < Position_Y < self.Planet_Eigenschaften[1]):
                    if (Position_X == 0):
                        # Liste - Startecken festlegen
                        Liste_Startecken.append((Liste_Startecken[(Position_Y - 1) * self.Planet_Eigenschaften[0]][3], Liste_Startecken[(Position_Y - 1) * self.Planet_Eigenschaften[0]][2], random.uniform(0, 1), random.uniform(0, 1)))
                    elif (Position_X == self.Planet_Eigenschaften[0] - 1):
                        # Liste - Startecken festlegen
                        Liste_Startecken.append((Liste_Startecken[(Position_Y - 1) * self.Planet_Eigenschaften[0] + Position_X][3], Liste_Startecken[(Position_Y - 1) * self.Planet_Eigenschaften[0] + Position_X][2], Liste_Startecken[Position_Y * self.Planet_Eigenschaften[0]][3], Liste_Startecken[Position_Y * self.Planet_Eigenschaften[0] + Position_X - 1][2]))
                    else:
                        # Liste - Startecken festlegen
                        Liste_Startecken.append((Liste_Startecken[(Position_Y - 1) * self.Planet_Eigenschaften[0] + Position_X][3], Liste_Startecken[(Position_Y - 1) * self.Planet_Eigenschaften[0] + Position_X][2], random.uniform(0, 1), Liste_Startecken[Position_Y * self.Planet_Eigenschaften[0] + Position_X - 1][2]))
                elif (Position_Y == self.Planet_Eigenschaften[1] - 1):
                    # Liste - Startecken festlegen
                    Liste_Startecken.append((Liste_Startecken[(Position_Y - 1) * self.Planet_Eigenschaften[0] + Position_X][3], Liste_Startecken[(Position_Y - 1) * self.Planet_Eigenschaften[0] + Position_X][2], Liste_Startecken[Position_X][1], Liste_Startecken[Position_X[0]]))

        # Rueckgabewert festlegen
        return Liste_Startecken

    def festlegen_eigenschaften(self, ID_Planet):
        # Anzahl - Biome - Horizontal festlegen
        Anzahl_Biome_Horizontal = {0: (4, 8)}

        # Anzahl - Biome - Vertikal festlegen
        Anzahl_Biome_Vertikal = {0: (2, 4)}

        # Rueckgabewert festlegen
        return (random.randint(Anzahl_Biome_Horizontal[ID_Planet][0], Anzahl_Biome_Horizontal[ID_Planet][1]), random.randint(Anzahl_Biome_Vertikal[ID_Planet][0], Anzahl_Biome_Vertikal[ID_Planet][1]))

    def festlegen_biom(self, Liste_Biomarten):
        for Position_Y in range(self.Planet_Eigenschaften[0]):
            for Position_X in range(self.Planet_Eigenschaften[1]):
                # Biomart festlegen
                Biomart = Liste_Biomarten[random.randint(0, len(Liste_Biomarten) - 1)]

                # Liste - Biome festlegen
                self.Liste_Biome[Position_X][Position_Y] = Biom(self.Seed_Planet, Biomart, self.festlegen_liste()[Position_Y * self.Planet_Eigenschaften[1] + Position_X])