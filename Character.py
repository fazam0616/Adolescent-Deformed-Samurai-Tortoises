import pygame


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.x)+", "+str(self.y)

class Character:
    baseImage = None
    frames1 = []
    frames2 = []
    health = 100
    rot = 0 #0 Points up, and rotation is counted clockwise
    speed = 5
    def __init__(self, wallMap, *point):
        self.wallMap = wallMap
        if len(point) == 2:
            self.pos = Point(point[0], point[1])
        else:
            self.pos = point[0]
    def imageSetup(self, name):
        self.baseImage = pygame.transform.scale(pygame.image.load("images\\"+name+"\\"+name+".png"), (100, 132))
        for i in range(10):
            self.frames1.append(
                pygame.transform.scale(pygame.image.load("images\\"+name+"\\"+name+"P" + str(i) + ".png"), (100, 132)))
    def move(self, delta):
        if self.wallMap[int((self.pos.x+delta.x)/50)][int((self.pos.y+delta.y)/50)] == False:
            self.pos.x += delta.x
            self.pos.y += delta.y
        if (abs(delta.x) < abs(delta.y)):
            self.rot = 0 if delta.y < 0 else 2
        else:
            self.rot = 1 if delta.x < 0 else 3


    def getPos(self):
        return self.pos.x, self.pos.y

    def getImage(self):
        return None