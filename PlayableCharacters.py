import imageio
import pygame

import Character

class Leo(Character.Character):
    def __init__(self, wallMap, waterMap, point):
        super().__init__(wallMap, waterMap, point)
        self.imageSetup("blue")
        self.damage = 5
        self.speed = 3

class Mike(Character.Character):
    def __init__(self, wallMap, waterMap, point):
        super().__init__(wallMap, waterMap, point)
        super().imageSetup("orange")
        self.damage = 2
        self.speed = 8

class Donny(Character.Character):
    def __init__(self, wallMap, waterMap, point):
        super().__init__(wallMap, waterMap, point)
        super().imageSetup("purple")
        self.damage = 2.5
        self.speed = 6

class Raph(Character.Character):
    def __init__(self, wallMap, waterMap, point):
        super().__init__(wallMap, waterMap, point)
        super().imageSetup("red")
        self.damage = 7
        self.speed = 1.5