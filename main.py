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
    bg = pygame.image.load("images\\world.png")

    player = PlayableCharacters.Leo(wallMap, Point(350,350))
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
            wallMap[int(x / 50)][int(y / 50)] = True if wallimage[y][x][0] == 64 else False

    for i in range(25):
        print(wallMap[i])
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
                    RIGHT = False
                    LEFT = False
                if event.key == pygame.K_s:
                    UP = False
                    DOWN = True
                    RIGHT = False
                    LEFT = False
                if event.key == pygame.K_d:
                    UP = False
                    DOWN = False
                    RIGHT = True
                    LEFT = False
                if event.key == pygame.K_a:
                    UP = False
                    DOWN = False
                    RIGHT = False
                    LEFT = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    UP = False
                if event.key == pygame.K_s:
                    DOWN = False
                if event.key == pygame.K_d:
                    RIGHT = False
                if event.key == pygame.K_a:
                    LEFT = False
        if UP:
            player.move(Point(0,-5))
        elif DOWN:
            player.move(Point(0,5))
        elif RIGHT:
            player.move(Point(5,0))
        elif LEFT:
            player.move(Point(-5,0))
        screen.fill((0,0,0))
        screen.blit(bg, (0, 0))
        screen.blit(player.getImage(),player.getPos())
        pygame.display.update()
        clock.tick(20)

main()