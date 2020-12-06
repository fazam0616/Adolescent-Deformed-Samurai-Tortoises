import Character

#here begins hunters shit code
class Enemy (Character.Character): #perhaps a character arg might be used... idk man im tired
    attack = 0

    def __init__(self, wallMap, *point):
        if len(point) == 2:
            super().__init__(wallMap, point[0], point[1])
        else:
            super().__init__(wallMap, point[0])
        super().imageSetup("black")

    def getImage(self):
        return pygame.transform.rotate(self.baseImage, (self.rot) * 90)