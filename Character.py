import main

class Character:
    health = 100
    def __init__(self, *point):
        if len(point) == 2:
            self.pos = main.Point(point[0], point[1])
        else:
            self.pos = point[0]

    def move(self, delta):
        if main.wallMap[self.pos.x+delta.x][self.pos.y+delta.y] == 0:
            self.pos.x += delta.x
            self.pos.y += delta.y
    def getImage(self):
        return None