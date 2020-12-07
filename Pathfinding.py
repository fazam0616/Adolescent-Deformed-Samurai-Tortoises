#Hunter's Code
#The pathfinding is kinda scuffed to avoid clumping of enemies and makes it look like its broken but its only kinda brokey
def setDirection(x,y, distToPlayer, bestDirArray, combineMap):  # takes the cordinates and sets a direction to the best next move... hunter doo doo code.. idrk where it goes...

    bestDist = distToPlayer[y - 1][x]  # checks the best distance in a square around it and sets the direction to move there
    bestDir = 'N'

    if ((distToPlayer[y][x + 1]) < bestDist):
        bestDist = distToPlayer[y][x + 1]
        bestDir = 'E'

    if ((distToPlayer[y + 1][x]) < bestDist):
        bestDist = distToPlayer[y + 1][x]
        bestDir = 'S'

    if ((distToPlayer[y][x - 1]) < bestDist):
        bestDist = distToPlayer[y][x - 1]
        bestDir = 'W'

    bestDirArray[y][x] = bestDir  # sets the cords of the best spot to the array
    if not combineMap[x][y]:
        return bestDist
    else:
        return bestDist + 9999 # makes terrrain a high dist so nothing paths to it

def spiralCheck(x,y, distToPlayer, combineMap, bestDirArray):
    if((x>=0 and x<=24) and (y>=0 and y<=24)):
        if not (wallMapG[x][y]):
            distToPlayer[y][x] = setDirection(x, y, distToPlayer, bestDirArray, combineMap) + 1  # set a pos in the array to the best direction and just so happens to return a value for distance to player
            if waterMapG[x][y]:
                distToPlayer[y][x] += 2 ## adjusts the severity of the water avoidance

# def setDist(playerPos, distToPlayer, combineMap, bestDirArray): # first iteration that doesnt really work that well
#     x = int(playerPos.x / 50)
#     y = int(playerPos.y / 50)
#
#     distToPlayer[y][x] = 0
#     dir='E' ## direction for the spiral to keep moving in when in terrain
#     OOB_count = 0  # out of bounds count
#     while (OOB_count < 50):  # makes it go in a spiral around the distance map
#
#         if ((x>0 and x<25) and (y>0 and y<25)) and not (combineMap[y][x]):
#             x += 1
#             spiralCheck(x, y, playerPos, distToPlayer, combineMap, bestDirArray)
#             while distToPlayer[y - 1][x] < 9999 and not combineMap[y - 1][x]:
#                 x += 1
#                 spiralCheck(x, y, playerPos, distToPlayer, combineMap, bestDirArray)
#                 OOB_count = int(0)
#                 dir = 'E'
#             y -= 1
#             spiralCheck(x, y, playerPos, distToPlayer, combineMap, bestDirArray)
#             while distToPlayer[y][x - 1] < 9999 and not combineMap[y][x - 1]:
#                 y -= 1
#                 spiralCheck(x, y, playerPos, distToPlayer, combineMap, bestDirArray)
#                 OOB_count = int(0)
#                 dir='N'
#             x -= 1
#             spiralCheck(x, y, playerPos, distToPlayer, combineMap, bestDirArray)
#             while distToPlayer[y + 1][x] < 9999 and not combineMap[y + 1][x]:
#                 x -= 1
#                 spiralCheck(x, y, playerPos, distToPlayer, combineMap, bestDirArray)
#                 OOB_count = int(0)
#                 dir='W'
#             y += 1
#             spiralCheck(x, y, playerPos, distToPlayer, combineMap, bestDirArray)
#             while distToPlayer[y][x + 1] < 9999 and not combineMap[y][x + 1]:
#                 y += 1
#                 spiralCheck(x, y, playerPos, distToPlayer, combineMap, bestDirArray)
#                 OOB_count = int(0)
#                 dir='S'
#         else:
#             OOB_count += 1
#             if dir == 'E':
#                 x+=1
#             elif dir == 'N':
#                 y-=1
#             elif dir == 'W':
#                 x-=1
#             elif dir == 'S':
#                 y+=1

def setDist2(playerPos, distToPlayer, combineMap, bestDirArray): # first iteration that doesnt really work that well
    for i in range(2): #runs it 5 times to deal with walls VERY INEFFICIENT
        x = int(playerPos.x / 50)
        y = int(playerPos.y / 50)

        distToPlayer[y][x] = 0
        bestDirArray[y][x] = 'P'
        radius=1

        while (radius<25): # loops in a spiral around the player position and filling in the dir map & dist map
            x+=1
            y-=1
            spiralCheck(x, y, distToPlayer, combineMap, bestDirArray)
            for i in range (0, radius*2):
                y+=1
                spiralCheck(x, y, distToPlayer, combineMap, bestDirArray)
            for i in range (0, radius*2):
                x-=1
                spiralCheck(x, y, distToPlayer, combineMap, bestDirArray)
            for i in range (0, radius*2):
                y-=1
                spiralCheck(x, y, distToPlayer, combineMap, bestDirArray)
            for i in range (0, radius*2):
                x+=1
                spiralCheck(x, y, distToPlayer, combineMap, bestDirArray)
            radius+=1
        none = None


def getVectorField(playerPos, wallMap, waterMap, enemyMap): #returns an array of cardinal directions whic hthe AI should follow to get to the player
    global waterMapG                                         # '0' is an unfiilled spot 'x' is a wall
    global combineMap
    global wallMapG
    wallMapG = wallMap
    waterMapG = waterMap
    bestDirArray = []

    combineMap = []

    for i in range(len(wallMap)):
        bestDirArray.append([])
        combineMap.append([])
        for x in range(len(wallMap[i])):
            bestDirArray[i].append(0)
            combineMap[i].append(False)

    for row in range(len(wallMap)):  # fills the array with a null value for terrain
        for column in range(len(wallMap[row])):
            if (wallMap[column][row] or enemyMap[column][row]):
                bestDirArray[row][column] = 'X'
            else:
                bestDirArray[column][row] = '0'
            if (wallMap[column][row] or enemyMap[column][row]): ## overides wall map with "terrain" for spots with too many enemies
                combineMap[column][row] = True


    distToPlayer = []
    for row in range(len(wallMap)):  # fills the array with a high value for the setDir to ignore unless it has been changed
        distToPlayer.append([])
        for column in range(len(wallMap[row])):
            distToPlayer[row].append(999999)


    setDist2(playerPos, distToPlayer, combineMap, bestDirArray)
    None # for debugging
    return bestDirArray