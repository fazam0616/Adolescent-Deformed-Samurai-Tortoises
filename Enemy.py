import pygame

import Character

#here begins hunters shit code
class Enemy (Character.Character): #perhaps a character arg might be used... idk man im tired
    attack = 0

    def __init__(self, wallMap, waterMap, enemyMap, point):
        self.enemyMap = enemyMap
        super().__init__(wallMap, waterMap, point)
        self.imageSetup("black")
        self.speed = 1
        self.enemyMap[int(self.pos.x/50)][int(self.pos.y/50)] += 1

    def moveD(self, dir):
        self.enemyMap[int(self.pos.x/50)][int(self.pos.y/50)] -= 1
        if dir != "0":
            if dir == "N":
                self.move(Character.Point(0, -self.speed))
            if dir == "S":
                self.move(Character.Point(0, self.speed))
            if dir == "E":
                self.move(Character.Point(self.speed,0))
            if dir == "W":
                self.move(Character.Point(-self.speed,0))

        self.enemyMap[int(self.pos.x/50)][int(self.pos.y/50)] += 1