from pygame import *

Width = 800
Height = 600
TILE = 32

window = display.set_mode((Width, Height))
display.set_caption('Танчики')

clock = time.Clock()
FPS = 60



class Tank():
    def __init__(self, color, px, py, direct, KeyList):
        object.append(self)
        self.type = 'tank'

        self.color = color
        self.rect = Rect(px, py, TILE,TILE)
        self.direct = direct
        self.moveSpeed = 2

        self.keyLEFT = KeyList[0]
        self.keyRIGHT = KeyList[1]
        self.keyUP = KeyList[2]
        self.keyDOWN = KeyList[3]
        self.keySHOT = KeyList[4]
    def update(self):
        if keys(self.keyLEFT):
            self.rect.x -= self.moveSpeed
        if keys(self.keyRIGHT):
            self.rect.x += self.moveSpeed
        if keys(self.keyUP):
            self.rect.y -= self.moveSpeed
        if keys(self.keyLEFT):
            self.rect.y += self.moveSpeed
    def draw(self):
        draw.rect(window, self.color, self.rect)

object = []
Tank('blue', 100, 275, 0, (K_a, K_d, K_w, K_s, K_SPACE))

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    keys = key.get_pressed()
    
    for obj in object: obj.update()
    window.fill((0,0,0))
    for obj in object: obj.draw()

    display.update()
    clock.tick(FPS)

