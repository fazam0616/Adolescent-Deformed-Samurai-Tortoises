def setDirection(playerPos, distToPlayer, bestDirArray):  # takes the cordinates and sets a direction to the best next move... hunter doo doo code.. idrk where it goes...
    x = int(playerPos.x / 50)
    y = int(playerPos.y / 50)

    bestDist = distToPlayer[x][
        y - 1]  # checks the best distance in a square around it and sets the direction to move there
    bestDir = 'N'
    tempX = x
    tempY = y - 1

    if ((distToPlayer[x + 1][y]) < bestDist):
        bestDist = distToPlayer[x + 1][y]
        bestDir = 'E'
        tempX = x + 1
        tempY = y

    if ((distToPlayer[x][y + 1]) < bestDist):
        bestDist = distToPlayer[x][y + 1]
        bestDir = 'S'
        tempX = x
        tempY = y + 1

    if ((distToPlayer[x - 1][y]) < bestDist):
        bestDist = distToPlayer[x - 1][y]
        bestDir = 'W'
        tempX = x - 1
        tempY = y

    bestDirArray[tempX][tempY] = bestDir  # sets the cords of the best spot to the array
    return bestDist

def spiralCheck(x,y, playerPos, distToPlayer, wallMap, bestDirArray):
    if not (wallMap[x][y]):  # starts the spiral to check squares
        distToPlayer[x][y] = setDirection(playerPos, distToPlayer, bestDirArray) + 1  # set a pos in the array to the best direction and just so happens to return a value for distance to player

def setDist(playerPos, distToPlayer, wallMap, bestDirArray):
    x = int(playerPos.x / 50)
    y = int(playerPos.y / 50)

    distToPlayer[x][y] = 0

    OOB_count = 0  # out of bounds count
    while (OOB_count < 15):  # makes it go i na spiral around the distance map
        if not wallMap[x][y]:
            x += 1
            while distToPlayer[x][y - 1] < 9999 and not wallMap[x][y - 1]:
                spiralCheck(x,y, playerPos, distToPlayer, wallMap, bestDirArray)
                x += 1
                OOB_count = 0
            y -= 1
            while distToPlayer[x - 1][y] < 9999 and not wallMap[x - 1][y]:
                spiralCheck(x,y, playerPos, distToPlayer, wallMap, bestDirArray)
                y -= 1
                OOB_count = 0
            x -= 1
            while distToPlayer[x][y + 1] < 9999 and not wallMap[x][y + 1]:
                spiralCheck(x,y, playerPos, distToPlayer, wallMap, bestDirArray)
                x -= 1
                OOB_count = 0
            y += 1
            while distToPlayer[x + 1][y] < 9999 and not wallMap[x + 1][y]:
                spiralCheck(x,y, playerPos, distToPlayer, wallMap, bestDirArray)
                y += 1
                OOB_count = 0
        OOB_count += 1



def getVectorField(playerPos, wallMap):
    bestDir = 'N'

    bestDirArray = []

    for i in range(len(wallMap)):
        bestDirArray.append([])
        for x in range(len(wallMap[i])):
            bestDirArray[i].append(0)

    for row in range(len(wallMap)):  # fills the array with a null value for terrain
        for column in range(len(wallMap[row])):
            if (wallMap[row][column]):
                bestDirArray[row][column] = None
            else:
                bestDirArray[row][column] = 'N'

    # x = 10
    # y = 10

    distToPlayer = []
    for row in range(len(wallMap)):  # fills the array with a high value for the setDir to ignore unless it has been changed
        distToPlayer.append([])
        for column in range(len(wallMap[row])):
            distToPlayer[row].append(999999)


    setDist(playerPos, distToPlayer, wallMap, bestDirArray)
    return bestDirArray