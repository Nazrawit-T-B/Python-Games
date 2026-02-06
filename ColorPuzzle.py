import pygame,sys,random 
from pygame.locals import *
pygame.init()

#Constants defining the width and height of parameters
Wwidth=640
Wheight=480
Box=60
Gap=10
NBoxesHorizontally=4
NBoxesVertically=4
Xmargin=int((Wwidth-(NBoxesHorizontally*(Box+Gap)))/2)
Ymargin=int((Wheight-(NBoxesVertically*(Box+Gap)))/2)

#Colors used repeatedly
WHITE=(255,255,255)
BLUE=(0,255,255)
GRAY=(100,100,100)
NAVY=(60,60,100)

BgColor=NAVY
LightBg=GRAY
BoxColor=WHITE
HighLightC=BLUE

def generateColors():
    return ((random.randint(0,255),random.randint(0,255),random.randint(0,255)))


def coloredSquares(screen):
    items=[]
    for i in range(5):
        for j in range(5):
            items.append(generateColors())
    random.shuffle(items)
    num=int(NBoxesHorizontally*NBoxesVertically/2)
    items=items[:num]*2
    random.shuffle(items)
    index = 0 
    for i in range(NBoxesHorizontally): 
        for j in range(NBoxesVertically): 
            x = Xmargin + i*(Box+Gap) 
            y = Ymargin + j*(Box+Gap) 
            rect = pygame.Rect(x, y, Box, Box) 
            pygame.draw.rect(screen, items[index], rect) 
            index += 1
    return 
#main game logic
def main():
    display=pygame.display.set_mode((Wwidth,Wheight))
    pygame.display.set_caption('Color Match')
    display.fill(LightBg)
    coloredSquares(display)
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__=='__main__':
    main()
