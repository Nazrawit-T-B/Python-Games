import pygame,sys,random
from pygame.locals import*
pygame.init()
backg=pygame.image.load('RatsAndCheese/image.png')
icon=pygame.image.load('RatsAndCheese/icons.png')
def main():
    display=pygame.display.set_mode((730,600))
    pygame.display.set_caption('Rats and Cheese')
    pygame.display.set_icon(icon)
    
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        display.blit(backg,(0,0))
        pygame.display.update()
if __name__=='__main__':
    main()
                