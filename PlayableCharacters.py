import imageio
import pygame

import Character

class Leo(Character.Character):
    def __init__(self, wallMap, waterMap, point):
        super().__init__(wallMap, waterMap, point)
        self.imageSetup("blue")
        self.damage = 50

class Mike(Character.Character):
    def __init__(self, wallMap, waterMap, point):
        super().__init__(wallMap, waterMap, point)
        super().imageSetup("orange")
        self.damage = 20
        self.speed = 6

class Donny(Character.Character):
    def __init__(self, wallMap, waterMap, point):
        super().__init__(wallMap, waterMap, point)
        super().imageSetup("purple")
        self.damage = 25
        self.speed = 8