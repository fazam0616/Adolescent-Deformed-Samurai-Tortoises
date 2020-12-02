class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.x)+", "+str(self.y)

class Character:
    health = 100
    def __init__(self, wallMap, *point):
        self.wallMap = wallMap
        if len(point) == 2:
            self.pos = Point(point[0], point[1])
        else:
            self.pos = point[0]

    def move(self, delta):
        if self.wallMap[int((self.pos.x+delta.x)/50)][int((self.pos.y+delta.y)/50)] == False:
            self.pos.x += delta.x
            self.pos.y += delta.y

    def getPos(self):
        return self.pos.x, self.pos.y

    def getImage(self):
        return None