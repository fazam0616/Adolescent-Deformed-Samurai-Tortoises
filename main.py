import sys

import pygame
import imageio
import PlayableCharacters
from Character import Point


def main(*args):
    global screen
    global wallMap
    # Initializing pygame internals and basic window setup
    pygame.init()

    width = 1280
    height = 1024

    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    wallimage = imageio.imread("images\\walls.bmp")
    wallMap = []

    player = PlayableCharacters.Leo(wallMap, Point(100,100))
    UP = False
    DOWN = False
    RIGHT = False
    LEFT = False

    for i in range(25):
        wallMap.append([])
        for x in range(25):
            wallMap[i].append(0)

    # Reading the wall map and creating a local version for look-up
    for x in range(0, 1250, 50):
        for y in range(0, 1250, 50):
            wallMap[int(x / 50)-1][int(y / 50)-1] = True if wallimage[x][y][0] != 0 else False

    #Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    UP = True
                    DOWN = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    UP = False

        if UP:
            player.move(Point(0,-5))

        screen.fill((0,0,0))
        screen.blit(player.getImage(),player.getPos())
        pygame.display.update()
        clock.tick(20)

main()