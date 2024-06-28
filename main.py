import pygame
from settings import *
import random
import time


def draw_background():
    screen.fill(BACKGROUND_COLOR)

def draw_button():
    pygame.draw.polygon(screen, GRAY, [(170,80), (410,80), (270,220), (10,220)])
    pygame.draw.polygon(screen, (100,0,0), [(150,100), (350,100), (250,200), (50,200)])
    pygame.draw.rect(screen, (100,0,0), (300,50,50,50))
    pygame.draw.rect(screen, (100,0,0), (50,150,50,50))
    pygame.draw.polygon(screen, RED, [(150,50), (350,50), (250,150), (50,150)])
    font = pygame.font.SysFont('arial', 30)
    text=font.render('Press me!', True, BLACK)
    screen.blit(text, (130,80))

def pressed():
    success_rate=100-count
    n=random.randint(1,100)
    if n<success_rate:
        success=True
    else:
        success=False
    update_stats(success)

def update_stats(success):
    pygame.draw.rect(screen, BROWN, (440,40,300,100))
    global count
    if success:
        count+=1
    else:
        count=0
    font = pygame.font.SysFont('arial', 25)
    text=font.render('Count: '+str(count), True, WHITE)
    screen.blit(text, (450,50))
    text=font.render('Success rate: '+str(100-count)+'%', True, WHITE)
    screen.blit(text, (450,80))



# def porb():
#     if count==0:
#         return(100)
#     else:
#         return()




if __name__=='__main__':

    pygame.init()
    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
    pygame.display.set_caption('Campo minato♥')
    font = pygame.font.SysFont('arial', 20)

    run  = True
    button=((50,350),(50,150))
    count=0

    draw_background()
    draw_button()
    update_stats(False)



    while run:

        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN or pygame.mouse.get_pressed()[0]:
                x,y=pygame.mouse.get_pos()
                if(x>button[0][0] and x<button[0][1] and y>button[1][0] and y<button[1][1]):
                    pressed()
                    # if count==0:
                    #     time.sleep(0.5)


        pygame.display.flip()
        clock.tick(30)
        

    pygame.quit()