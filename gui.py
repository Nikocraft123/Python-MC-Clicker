# IMPORTS
import pygame as pg
from general import *


# CLASSES

# GUI
class GUI:

    # CONSTRUCTOR
    def __init__(self):

        # Initialize pygame
        pg.init()
        pg.display.set_caption(f"{NAME} (by {AUTHOR}) v{VERSION}")

        # Window information
        self.screen = pg.Surface(WINDOW_DIM)
        self.clock = pg.time.Clock()
        self.running = False


    # METHODS


