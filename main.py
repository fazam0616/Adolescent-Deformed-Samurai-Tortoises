import sys
from time import sleep

import pygame
import imageio
import Character

#Initializing pygame internals and basic window setup
pygame.init()
width = 1280
height = 1024
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
wallimage = imageio.imread("images\\walls.bmp")
wallMap = []

for i in range(25):
    wallMap.append([])
    for x in range(25):
        wallMap[i].append(0)

#Reading the wall map and creating a local version for look-up
for x in range(0,1250,50):
    for y in  range(0,1250,50):
        #print(x,y)
        wallMap[int(x/50)][int(y/50)] = True if wallimage[x][y][0] != 0 else False


#Basic Classes
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.x)+", "+str(self.y)

#Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,255))
    pygame.display.update()
    clock.tick(20)