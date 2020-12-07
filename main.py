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
def distance(pos1, pos2):
    return (pos1.x - pos2.x)**2 + (pos1.y - pos2.y)**2


def main(*args):
    global screen
    global wallMap
    global offset
    global mag

    # Initializing pygame internals and basic window setup
    pygame.init()
    pygame.font.init()
    myfont = pygame.font.SysFont('Arial', 20)
    enemCount = pygame.font.SysFont('Arial', 10)

    mag = 1.25
    width = 1280
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Adolescent Deformed Samurai Tortoises")

    clock = pygame.time.Clock()

    wallimage = imageio.imread("images\\walls.bmp")
    waterimage = imageio.imread("images\\water.bmp")
    wallMap = []
    waterMap =[]
    enemyMap = []
    enemyTruthMap = []
    damageMap = []
    bg = pygame.transform.scale(pygame.image.load("images\\world.png"),(int(len(wallimage[0])*mag),int(len(wallimage[0])*mag)))
    wave = 0
    remainSpawn = 2**wave
    spawns = [Point(12,1),Point(12,23),Point(1,16),Point(23,9)]
    maxEnemDen = 4
    killCount = 0

    #Camera offset initialization
    offset = Point(0,0)

    if (args[0]=="blue"):
        player = PlayableCharacters.Leo(wallMap, waterMap, Point(1250/2,600/2))
    elif (args[0]=="red"):
        player = PlayableCharacters.Raph(wallMap, waterMap, Point(1250/2,600/2))
    elif (args[0]=="orange"):
        player = PlayableCharacters.Mike(wallMap, waterMap, Point(1250/2,600/2))
    elif (args[0]=="purple"):
        player = PlayableCharacters.Donny(wallMap, waterMap, Point(1250/2,600/2))

    #Boolean flags for movement. Rudimentary but they do the trick
    UP = False
    DOWN = False
    RIGHT = False
    LEFT = False

    #Enables debug visuals
    DEBUG = False

    #Creation of empty wall map lookup
    for row in range(25):
        wallMap.append([])
        waterMap.append([])
        enemyMap.append([])
        enemyTruthMap.append([])
        damageMap.append([])
        for x in range(25):
            wallMap[row].append(0)
            waterMap[row].append(0)
            enemyMap[row].append(0)
            enemyTruthMap[row].append(0)
            damageMap[row].append(0)

    # Reading the wall map and creating a local version for look-up
    for x in range(0, len(wallimage[0]), 50):
        for y in range(0, len(wallimage[0]), 50):
            wallMap[int(x / 50)][int(y / 50)] = True if wallimage[y+25][x+25][0] == 64 else False
            waterMap[int(x / 50)][int(y / 50)] = True if waterimage[y+25][x+25][2] != 0 else False

    enemies = []

    # for row in range(50):
    #     enemies.append(Enemy.Enemy(wallMap, waterMap, enemyMap, Point(
    #         random.randrange(50,1200),
    #         random.randrange(50,1200))))

    #Game loop
    while True:
        if player.health > 0:
            #Going through game events
            for event in pygame.event.get():
                #If the "X" button is clicked
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if player.attack == 0:
                        deltaX = pygame.mouse.get_pos()[0]-(calcScreenPos(player)[0]+player.getImage(mag).get_size()[0]/2)
                        deltaY = pygame.mouse.get_pos()[1]-(calcScreenPos(player)[1]+player.getImage(mag).get_size()[1]/2)
                        if (abs(deltaX) >= abs(deltaY)):
                            if deltaX > 0:
                                LEFT = False
                                player.rot = 3
                                damageMap[int(player.pos.x/50)+1][int(player.pos.y/50)] = player.damage
                            else:
                                RIGHT = False
                                player.rot = 1
                                damageMap[int(player.pos.x/50)-1][int(player.pos.y/50)] = player.damage
                        else:
                            if deltaY > 0:
                                UP = False
                                player.rot = 2
                                damageMap[int(player.pos.x/50)][int(player.pos.y/50)+1] = player.damage
                            else:
                                DOWN = False
                                player.rot = 0
                                damageMap[int(player.pos.x/50)][int(player.pos.y/50)-1] = player.damage

                        damageMap[int(player.pos.x / 50)][int(player.pos.y / 50)] = player.damage
                        player.attack = 1
                #If a key is pressed/unpressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_v:
                        DEBUG = not DEBUG
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

            #Spawning enemies at start of round
            if len(enemies) == 0:
                wave += 1
                remainSpawn = 2**wave
                for row in enemyMap:
                    for column in range(len(row)):
                        row[column] = 0
            if (remainSpawn > 0):
                for i in range(remainSpawn):
                    availSpawn = []
                    for point in spawns:
                        if enemyMap[point.x][point.y] < 1:
                            availSpawn.append(point)
                    if (len(availSpawn) > 0):
                        spawn = random.choice(availSpawn).__copy__()
                        remainSpawn -= 1
                        spawn.x *= 50
                        spawn.y *= 50
                        enemy = Enemy.Enemy(wallMap, waterMap, enemyMap, spawn)
                        enemies.append(enemy)
                    else:
                        break

            """
            Only one form of movement is allowed at a time, in order to allow
            for basic 90 degree angles in all calcs. 
            """

            if UP:
                #Move player
                player.move(Point(0,-player.speed))

                #Fix camera offset
                if player.pos.y * mag - offset.y < width*0.1:
                    if offset.y > 0:
                        offset.y = -(width*0.1-(player.pos.y * mag))
            elif DOWN:
                #Move player
                player.move(Point(0,player.speed))

                #Fix camera offset
                if player.pos.y * mag - offset.y > height - width*0.1:
                    if offset.y < len(wallimage[0])*mag-height:
                        offset.y = -(height - width*0.1-(player.pos.y * mag))
            elif RIGHT:
                #Move player
                player.move(Point(player.speed,0))

                #Fix camera offset
                if player.pos.x * mag - offset.x > width - width*0.15:
                    if offset.x < len(wallimage[0])*mag-width:
                        offset.x = -(width - width*0.15 - (player.pos.x * mag))
            elif LEFT:
                #Move player
                player.move(Point(-player.speed,0))

                #Fix camera offset
                if player.pos.x * mag - offset.x < width*0.15:
                    if offset.x > 0:
                        offset.x = player.pos.x*mag-width*0.15
            for x in range(25):
                for y in range(25):
                    enemyTruthMap[x][y] = enemyMap[x][y] > maxEnemDen

            for row in range(len(damageMap)):
                for column in range(len(damageMap[row])):
                    if player.attack == 0:
                        damageMap[row][column] = 0

            dirMap = Pathfinding.getVectorField(player.pos, wallMap, waterMap, enemyMap)

            # Fill the screen with black to clear off last frame
            screen.fill((0, 0, 0))

            # Draw map with offset
            screen.blit(bg, (int(round(-offset.x)), int(round(-offset.y))))
            if DEBUG:
                debugDraw(bg, player, enemies, damageMap, dirMap, myfont, enemyMap)

            for enemy in enemies:
                if enemy.health>0:
                    enemy.moveD(dirMap[int(enemy.pos.y/50)][int(enemy.pos.x/50)])
                    dam = damageMap[int(enemy.pos.x/50)][int(enemy.pos.y/50)]
                    enemy.health -= dam
                    pos = list(calcScreenPos(enemy))
                    screen.blit(enemy.getImage(mag), pos)
                    if distance(player.pos,enemy.pos) < 40**2 and enemy.attack == 0:
                        player.health -= 10
                        enemy.attack = 1
                    pos[0] += enemy.getImage(mag).get_size()[0]/2 - 15
                    pos[1] += enemy.getImage(mag).get_size()[1]/2 - 10
                    enemHealth = myfont.render(str(enemy.health),False,(255,0,0))
                    screen.blit(enemHealth, pos)
                else:
                    killCount += 1
                    enemyMap[int(enemy.pos.x/50)][int(enemy.pos.y/50)] -= 1
                    enemies.remove(enemy)


            #Draw player
            screen.blit(player.getImage(mag), calcScreenPos(player))

            #Drawing health bar
            pygame.draw.rect(screen,(255,0,0),((1250*0.3/2,10),(1260*(2/3),20)))
            pygame.draw.rect(screen,(0,255,0),((1250*0.3/2,10),(1260*(2/3)*(abs(player.health)/100),20)))

            #Updating display and ticking internal game clock
            fpsCounter = myfont.render("FPS: "+str(int(clock.get_fps())), False, (0,255,0))
            enemyCount = myfont.render("Enemy Count: "+str(len(enemies)), False, (0,255,0))
            screen.blit(fpsCounter, (0,0))
            screen.blit(enemyCount, (0,25))
            clock.tick(60)
            pygame.display.update()
        else:
            # Ending the game
            print("You died, after killing " + str(killCount) + " members of the toe clan!")
            pygame.quit()
            break

def debugDraw(bg, player, enemies, damageMap, dirMap, myfont, enemyMap):

    # Draw player pos
    pygame.draw.rect(screen, (0, 0, 255), [
        [int(player.pos.x / 50) * 50 * mag - offset.x, int(player.pos.y / 50) * 50 * mag - offset.y],
        [25 * mag, 50 * mag]])

    # Draw square to show enemy pos
    for enemy in enemies:
        pygame.draw.rect(screen, (0, 255, 0), [
            [int(enemy.pos.x / 50) * 50 * mag - offset.x + 25 * mag, int(enemy.pos.y / 50) * 50 * mag - offset.y],
            [25 * mag, 50 * mag]])

    # Draw grid lines and damage squares:
    for x in range(len(damageMap)):
        pygame.draw.line(screen, (0, 0, 0), ((x * 50 * mag - offset.x), 0), ((x * 50 * mag - offset.x), 600))
        pygame.draw.line(screen, (0, 0, 0), (0, (x * 50 * mag - offset.y)), (1250, (x * 50 * mag - offset.y)))
        for y in range(len(damageMap[x])):
            if damageMap[x][y] != 0:
                pygame.draw.rect(screen, (255, 0, 0), [[x * 50 * mag - offset.x + 10, y * 50 * mag - offset.y + 10],
                                                           [50 * mag - 20, 50 * mag - 20]])

    # Draw pathfinding arrows
    for x in range(len(damageMap)):
        for y in range(len(damageMap[x])):
            if dirMap[x][y] != 0:
                enemDens = myfont.render(str(enemyMap[x][y]), False, (255, 0, 0))
                screen.blit(enemDens, (int((x * 50 + 40) * mag - offset.x), int((y * 50) * mag - offset.y)))
                if (dirMap[x][y] == "N"):
                    pygame.draw.line(screen, (255, 255, 255),
                                     ((x * 50 + 25) * mag - offset.x, (y * 50 + 10) * mag - offset.y),
                                     ((x * 50 + 25) * mag - offset.x, (y * 50 + 40) * mag - offset.y))
                    pygame.draw.circle(screen, (255, 255, 255),
                                       (int((x * 50 + 25) * mag - offset.x), int((y * 50 + 40) * mag - offset.y)),
                                       3)
                if (dirMap[x][y] == "S"):
                    pygame.draw.line(screen, (255, 255, 255),
                                     ((x * 50 + 25) * mag - offset.x, (y * 50 + 10) * mag - offset.y),
                                     ((x * 50 + 25) * mag - offset.x, (y * 50 + 40) * mag - offset.y))
                    pygame.draw.circle(screen, (255, 255, 255),
                                       (int((x * 50 + 25) * mag - offset.x), int((y * 50 + 10) * mag - offset.y)),
                                       3)
                if (dirMap[x][y] == "E"):
                    pygame.draw.line(screen, (255, 255, 255),
                                     ((x * 50 + 10) * mag - offset.x, (y * 50 + 25) * mag - offset.y),
                                     ((x * 50 + 40) * mag - offset.x, (y * 50 + 25) * mag - offset.y))
                    pygame.draw.circle(screen, (255, 255, 255),
                                       (int((x * 50 + 10) * mag - offset.x), int((y * 50 + 25) * mag - offset.y)),
                                       3)
                if (dirMap[x][y] == "W"):
                    pygame.draw.line(screen, (255, 255, 255),
                                     ((x * 50 + 10) * mag - offset.x, (y * 50 + 25) * mag - offset.y),
                                     ((x * 50 + 40) * mag - offset.x, (y * 50 + 25) * mag - offset.y))
                    pygame.draw.circle(screen, (255, 255, 255),
                                       (int((x * 50 + 40) * mag - offset.x), int((y * 50 + 25) * mag - offset.y)),
                                       3)