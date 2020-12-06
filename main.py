import sys
import Enemy
import imageio
import pygame
import random
import Pathfinding

import PlayableCharacters
from Character import Point
"""
Method for getting players on screen position with the cam-offset
applied. Allows for finding the position of the camera that dis-allows off camera players
"""
def calcScreenPos(player):
    #The screen is magnified by 1.75
    x = player.pos.x*mag
    y = player.pos.y*mag

    x -= offset.x
    y -= offset.y

    #Offset by players size
    x -= player.getImage(mag).get_width()/2
    y -= player.getImage(mag).get_height()/2

    return (int(x),int(y))

#Main game funcion called by Menu.py
def main(*args):
    global screen
    global wallMap
    global offset
    global mag

    # Initializing pygame internals and basic window setup
    pygame.init()

    mag = 1.25
    width = 1280
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Adolescent Deformed Samurai Tortoises")

    clock = pygame.time.Clock()

    wallimage = imageio.imread("images\\walls.bmp")
    waterimage = imageio.imread("images\\water.bmp")
    wallMap = []
    watermap =[]
    bg = pygame.transform.scale(pygame.image.load("images\\world.png"),(int(len(wallimage[0])*mag),int(len(wallimage[0])*mag)))

    #Camera offset initialization
    offset = Point(0,0)

    player = PlayableCharacters.Leo(wallMap, watermap, Point(100,100))

    #Boolean flags for movement. Rudimentary but they do the trick
    UP = False
    DOWN = False
    RIGHT = False
    LEFT = False

    #Creation of empty wall map lookup
    for i in range(25):
        wallMap.append([])
        watermap.append([])
        for x in range(25):
            wallMap[i].append(0)
            watermap[i].append(0)

    # Reading the wall map and creating a local version for look-up
    for x in range(0, len(wallimage[0]), 50):
        for y in range(0, len(wallimage[0]), 50):
            wallMap[int(x / 50)][int(y / 50)] = True if wallimage[y+25][x+25][0] == 64 else False
            watermap[int(x / 50)][int(y / 50)] = True if waterimage[y+25][x+25][2] != 0 else False

    for i in range(25):
        print(watermap[i])

    enemies = []

    for i in range(15):
        enemies.append(Enemy.Enemy(wallMap, watermap, Point(
            random.randrange(50,1200),
            random.randrange(50,1200))))

    #Game loop
    while True:
        #Going through game events
        for event in pygame.event.get():
            #If the "X" button is clicked
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #If a key is pressed/unpressed
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

        """
        Only one form of movement is allowed at a time, in order to allow
        for basic 90 degree angles in all calcs. 
        """
        pSpeed = player.speed * (0.5 if watermap[int((player.pos.x)/50)][int((player.pos.y)/50)] else 1)
        if UP:
            #Move player
            player.move(Point(0,-player.speed))

            #Fix camera offset
            if player.pos.y * mag - offset.y < height * 0.3:
                if offset.y > 0:
                    offset.y -= pSpeed*2
        elif DOWN:
            #Move player
            player.move(Point(0,player.speed))

            #Fix camera offset
            if player.pos.y * mag - offset.y > height * 0.7:
                if offset.y < len(wallimage[0])*mag-height:
                    offset.y += pSpeed*2
        elif RIGHT:
            #Move player
            player.move(Point(player.speed,0))

            #Fix camera offset
            if player.pos.x * mag - offset.x > width * 0.85:
                if offset.x < len(wallimage[0])*mag-width:
                    offset.x += pSpeed*2
        elif LEFT:
            #Move player
            player.move(Point(-player.speed,0))

            #Fix camera offset
            if player.pos.x * mag - offset.x < width * 0.15:
                if offset.x > 0:
                    offset.x -= pSpeed*2

        dirMap = Pathfinding.getVectorField(player.pos, wallMap, watermap)

        # for i in dirMap:
        #     print(i)
        # print("-----------------------------------------------------------------------")

        #Fill the screen with black to clear off last frame
        screen.fill((0,0,0))

        #Draw map with offset
        screen.blit(bg, (-offset.x, -offset.y))

        for enemy in enemies:
            enemy.moveD(dirMap[int(enemy.pos.y/50)][int(enemy.pos.x/50)])
            screen.blit(enemy.getImage(mag), calcScreenPos(enemy))

        #Draw player
        screen.blit(player.getImage(mag), calcScreenPos(player))

        #Updating display and ticking internal game clock
        pygame.display.update()
        clock.tick(60)


main()
#bruh=Enemy.__init__(wallMap)