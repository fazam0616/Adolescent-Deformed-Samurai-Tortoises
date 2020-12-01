import pygame
import imageio
import Character

#Initializing pygame internals and basic window setup
pygame.init()
width = 1280
height = 1024
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
wallMap = imageio.imread()

#Basic Classes
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.x)+", "+str(self.y)


