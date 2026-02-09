import pygame,sys,random
from pygame.locals import*
pygame.init()
backg=pygame.image.load('RatsAndCheese/background.png')
def main():
    display=pygame.display.set_mode((640,480))
    pygame.display.set_caption('Rats and Cheese')
    display.blit(backg,(0,0))
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
if __name__=='__main__':
    main()
                