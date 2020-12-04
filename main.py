import sys

import imageio
import pygame

import PlayableCharacters
from Character import Point

#import Enemy


def calcPlayerPos(player):
    x = player.pos.x*2
    y = player.pos.y*2

    x -= offset.x
    y -= offset.y

    x -= player.getImage().get_width()/2
    y -= player.getImage().get_height()/2

    return (int(x),int(y))


def main(*args):
    global screen
    global wallMap
    global offset
    # Initializing pygame internals and basic window setup
    pygame.init()

    width = 1280
    height = 600

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Adolescent Deformed Samurai Tortoises")
    clock = pygame.time.Clock()
    wallimage = imageio.imread("images\\walls.bmp")
    wallMap = []
    bg = pygame.transform.scale(pygame.image.load("images\\world.png"),(2500,2500))
    offset = Point(0,0)

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
            wallMap[int(x / 50)][int(y / 50)] = True if wallimage[y+25][x+25][0] == 64 else False

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
            player.move(Point(0,-player.speed))
            if player.pos.y * 2 - offset.y < height * 0.3:
                if offset.y > 0:
                    offset.y -= player.speed*2
        elif DOWN:
            player.move(Point(0,player.speed))
            if player.pos.y * 2 - offset.y > height * 0.7:
                if offset.y < 1900:
                    offset.y += player.speed*2
        elif RIGHT:
            player.move(Point(player.speed,0))
            if player.pos.x * 2 - offset.x > width * 0.85:
                if offset.x < 1220:
                    offset.x += player.speed*2
        elif LEFT:
            player.move(Point(-player.speed,0))
            if player.pos.x * 2 - offset.x < width * 0.15:
                if offset.x > 0:
                    offset.x -= player.speed*2
        screen.fill((0,0,0))
        screen.blit(bg, (-offset.x, -offset.y))
        screen.blit(player.getImage(),calcPlayerPos(player))
        pygame.display.update()
        clock.tick(20)

main()
#bruh=Enemy.__init__(wallMap)