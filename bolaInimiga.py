import random
class BolaInimiga:
    posi = []
    destino = []
    x = 0
    y = 0

    def __init__(self, ScreenSize):
        positions = [[0,random.randint(0,ScreenSize[1])],[ScreenSize[0],random.randint(0,ScreenSize[1])],[random.randint(0,ScreenSize[0]),0],[random.randint(0,ScreenSize[0]),ScreenSize[1]]]
        destiny = [[ScreenSize[0], random.randint(0, ScreenSize[1])], [0, random.randint(0, ScreenSize[1])], [random.randint(0, ScreenSize[0]), ScreenSize[1]],[random.randint(0, ScreenSize[0]), 0]]

        indice = random.randint(0,3)
        self.posi = positions[indice]
        self.destino = destiny[indice]

        self.x = (self.destino[0] - self.posi[0]) / 1500
        self.y = (self.destino[1] - self.posi[1]) / 1500





    def move(self):
        self.posi[0] += self.x
        self.posi[1] += self.y


    def destroy(self, gameAreaSize):
        fora = False
        if self.posi[0] > gameAreaSize[0] or self.posi[0] < 0 or self.posi[1] > gameAreaSize[1] or self.posi[1] < 0:
            fora = True

        return fora



