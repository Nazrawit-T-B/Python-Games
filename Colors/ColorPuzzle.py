import pygame,sys,random 
from pygame.locals import *
pygame.init()

#Constants defining the width and height of parameters
Wwidth=640
Wheight=480
Box=80
Gap=10
NBoxesHorizontally=4
NBoxesVertically=4
showing_time=8
Xmargin=int((Wwidth-(NBoxesHorizontally*(Box+Gap)))/2)
Ymargin=int((Wheight-(NBoxesVertically*(Box+Gap)))/2)

#Colors used repeatedly
WHITE=(255,255,255)
BLUE=(0,255,255)
GRAY=(100,100,100)
NAVY=(60,60,100)
BLACK=(0,0,0)
BgColor=NAVY
LightBg=GRAY
BoxColor=BLACK
HighLightC=BLUE
icon=pygame.image.load('Colors\icon.png')

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
    board=[]
    index = 0 
    for j in range(NBoxesVertically): 
        column=[]
        for i in range(NBoxesHorizontally): 
            x = Xmargin + i*(Box+Gap) 
            y = Ymargin + j*(Box+Gap) 
            rect = pygame.Rect(x, y, Box, Box) 
            pygame.draw.rect(screen, items[index], rect,border_radius=5) 
            column.append(items[index])
            index += 1
        board.append(column)
            
    return board
def coverSquares(screen):
    #logic that covers the squares created after some while time
    #creates the squares and then covers them in this function 
    board=coloredSquares(screen)
    pygame.display.update()
    pygame.time.delay(3000)
    clock=pygame.time.Clock()
    #cover all the square to black
    for i in range(NBoxesHorizontally):
        for j in range(NBoxesVertically):
            x = Xmargin + i*(Box+Gap) 
            y = Ymargin + j*(Box+Gap) 
            rect = pygame.Rect(x, y, Box, Box) 
            pygame.draw.rect(screen, NAVY, rect,border_radius=5) 
    pygame.display.update(rect)
    #clock.tick(50)
    return board

def hasWon(matched):
    for row in matched:
        if False in row:
            return False
    return True 
#main game logic
def main():
    display=pygame.display.set_mode((Wwidth,Wheight))
    pygame.display.set_caption('Color Match')
    pygame.display.set_icon(icon)
    display.fill(WHITE)
    board=coverSquares(display)
    start_time=pygame.time.get_ticks()
    #create an event that detects a cursor action and behaves
    revealed=[[False]*NBoxesHorizontally for i in range(NBoxesVertically)]
    matched=[[False]*NBoxesHorizontally for i in range(NBoxesVertically)]
    selected=[]
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEBUTTONDOWN:
                x,y=event.pos
                for i in range(NBoxesHorizontally):
                    for j in range(NBoxesVertically):
                        box_x = Xmargin + i*(Box+Gap) 
                        box_y = Ymargin + j*(Box+Gap) 
                        if box_x <= x < box_x + Box and box_y <= y < box_y + Box:
                            if not revealed[j][i] and not matched[j][i]:
                                revealed[j][i] = True
                                selected.append((j, i))
                                rect = pygame.Rect(box_x, box_y, Box, Box) 
                                pygame.draw.rect(display, board[j][i], rect,border_radius=5) 
                                pygame.display.update(rect)
                                if len(selected) == 2:
                                    j1, i1 = selected[0]
                                    j2, i2 = selected[1]
                                    if board[j1][i1] == board[j2][i2]:
                                        matched[j1][i1] = True
                                        matched[j2][i2] = True
                                    else:
                                        pygame.time.delay(1000)
                                        for j_sel, i_sel in selected:
                                            revealed[j_sel][i_sel] = False
                                            box_x_sel = Xmargin + i_sel*(Box+Gap) 
                                            box_y_sel = Ymargin + j_sel*(Box+Gap) 
                                            rect_sel = pygame.Rect(box_x_sel, box_y_sel, Box, Box) 
                                            pygame.draw.rect(display, NAVY, rect_sel,border_radius=5) 
                                            pygame.display.update(rect_sel)
                                    selected.clear()
        pygame.display.update()

if __name__=='__main__':
    main()
