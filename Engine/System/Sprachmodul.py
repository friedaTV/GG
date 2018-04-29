def sprachmodul_laden(ID_Programmsprache):
    # Pruefen, welche Programmsprache ausgewaehlt wurde
    if (ID_Programmsprache == 0):
        # Sprachmodul festlegen
        from Konfiguration.__SprLi__ import __DE__ as Sprachmodul
    else:
        # Sprachmodul festlegen
        Sprachmodul = None

    # Rueckgabewert festlegen
    return Sprachmodul