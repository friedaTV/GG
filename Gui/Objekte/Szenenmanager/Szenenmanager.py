class Szenenmanager:
    def __init__(self):
        # Liste - Szenenmanager festlegen
        self.Liste_Szenenmanager = []

    def laden_szene(self):
        # Szene - Intro festlegen
        Szene_Intro = None

        # Szene - Option festlegen
        Szene_Option = None

        # Szene - Spielwelt festlegen
        Szene_Spielwelt = None

        # Liste - Szenenmanager festlegen
        self.Liste_Szenenmanager.append(Szene_Intro)
        self.Liste_Szenenmanager.append(Szene_Option)
        self.Liste_Szenenmanager.append(Szene_Spielwelt)

    def festlegen_szene(self, ID_Szene):
        # Rueckgabewert festlegen
        return self.Liste_Szenenmanager[ID_Szene]