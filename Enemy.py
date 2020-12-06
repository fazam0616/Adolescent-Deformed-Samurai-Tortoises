import pygame

import Character

#here begins hunters shit code
class Enemy (Character.Character): #perhaps a character arg might be used... idk man im tired
    attack = 0

    def __init__(self, wallMap, waterMap, *point):
        if len(point) == 2:
            super().__init__(wallMap, waterMap, point[0], point[1])
        else:
            super().__init__(wallMap, waterMap, point[0])
        super().imageSetup("black")
        self.speed = 1

    def moveD(self, dir):
        if dir != "0":
            if dir == "N":
                self.move(Character.Point(0, -self.speed))
            if dir == "S":
                self.move(Character.Point(0, self.speed))
            if dir == "E":
                self.move(Character.Point(self.speed,0))
            if dir == "W":
                self.move(Character.Point(-self.speed,0))