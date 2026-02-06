import pygame,sys,random 
from pygame.locals import *
pygame.init()

#Constants defining the width and height of parameters
Wwidth=640
Wheight=480
Box=40
Gap=10
NBoxesHorizontally=10
NBoxesVertically=7
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
    return ((random.randint(0,255),random.randint(0,255),random.rantint(0,255)))

def main():
    display=pygame.display.set_mode((Wwidth,Wheight))
    display.fill(BgColor)
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__=='__main__':
    main()
