import imageio
import pygame

import Character

class Leo(Character.Character):
    attack = 0
    def __init__(self, wallMap, waterMap, *point):
        if len(point)==2:
            super().__init__(wallMap, waterMap, point[0],point[1])
        else:
            super().__init__(wallMap, waterMap, point[0])
        super().imageSetup("blue")
\\

