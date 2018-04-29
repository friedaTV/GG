# Impor - Modul: pygame
import pygame

# Import - Modul: Spielclient
from Gui.Spielclient.Spielclient.Spielclient import Spielclient

# PyGame festlegen
pygame.init()

# Client festlegen
Client = Spielclient()

# Programmschleife festlegen
Client.programmschleife()