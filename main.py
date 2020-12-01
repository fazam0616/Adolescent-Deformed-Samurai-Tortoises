import pygame

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.x)+", "+str(self.y)


class Character:
    health = 100
    def __init__(self, *point):
        if len(point) == 2:
            self.pos = Point(point[0], point[1])
        else:
            self.pos = point[0]

a = Character(1,1)
c = Character(Point(2,2))

print(a.pos)
print(c)