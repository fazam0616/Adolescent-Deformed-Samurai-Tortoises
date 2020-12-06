import imageio
import pygame

import Character

class Leo(Character.Character):
    attack = 0
    def __init__(self, wallMap, *point):
        if len(point)==2:
            super().__init__(wallMap, point[0],point[1])
        else:
            super().__init__(wallMap, point[0])
        super().imageSetup("blue")


    def getImage(self):
        return pygame.transform.rotate(self.baseImage,(self.rot)*90)