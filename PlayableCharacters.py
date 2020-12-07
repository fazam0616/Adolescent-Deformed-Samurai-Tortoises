import imageio
import pygame

import Character

class Leo(Character.Character):
    attack = 0
    def __init__(self, wallMap, waterMap, point):
        super().__init__(wallMap, waterMap, point)
        super().imageSetup("blue")


