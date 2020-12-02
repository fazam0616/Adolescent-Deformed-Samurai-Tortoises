import imageio
import pygame

import Character

class Leo(Character.Character):
    def __init__(self, wallMap, *point):
        if len(point)==2:
            super().__init__(wallMap, point[0],point[1])
        else:
            super().__init__(wallMap, point[0])
    def getImage(self):
        return pygame.transform.scale(pygame.image.load("images\\Blue\\blue.png"),(50,66)) #TERRIBLE FOR FRAMES. PRECALCULATE AT STARTUP AND STORE EACH FRAME INSTEAD