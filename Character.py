import pygame


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.x)+", "+str(self.y)
    def __copy__(self):
        return Point(self.x, self.y)

class Character:
    def __init__(self, wallMap, waterMap, point):
        self.baseImage = None
        self.frames1 = []
        self.frames2 = []
        self.health = 100
        self.rot = 0 #0 Points up, and rotation is counted clockwise from there to a max of 3
        self.speed = 3
        self.currentFrame = 0
        self.attack = 0
        self.frame = 0
        self.damage = 0
        self.wallMap = wallMap
        self.watermap = waterMap
        self.pos = point

    def imageSetup(self, name):
        self.baseImage = pygame.image.load("images\\"+name+"\\"+name+".png")

        #Reading in attack animations
        for i in range(10):
         self.frames1.append(
             pygame.image.load("images\\"+name+"\\"+name+"P" + str(i) + ".png"))
    def move(self, delta):
        #Making sure the destination tile isn't a wall
        if self.wallMap[int((self.pos.x+delta.x)/50)][int((self.pos.y+delta.y)/50)] == False:
            if self.watermap[int((self.pos.x+delta.x)/50)][int((self.pos.y+delta.y)/50)] == False:
                self.pos.x += delta.x
                self.pos.y += delta.y
            else:
                self.pos.x += delta.x * 0.5
                self.pos.y += delta.y * 0.5


        #Fixing orientation
        if (abs(delta.x) < abs(delta.y)):
            self.rot = 0 if delta.y < 0 else 2
        else:
            self.rot = 1 if delta.x < 0 else 3


    def getPos(self):
        return self.pos.x, self.pos.y

    def getImage(self, mag):
        if self.attack == 0:
            img = pygame.transform.scale(self.baseImage,(int(self.baseImage.get_size()[0]*mag/4),int(self.baseImage.get_size()[1]*mag/4)))
        else:
            temp = self.frames1[int(self.frame)]
            img = pygame.transform.scale(temp,(int(temp.get_size()[0]*mag/4),int(temp.get_size()[1]*mag/4)))
        self.frame += 0.1
        if self.frame >= 9:
            self.frame = 0
            self.attack = 0
        return pygame.transform.rotate(img,(self.rot)*90)