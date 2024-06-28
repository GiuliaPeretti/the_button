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
    update_record()
    draw_progress_bar()

def update_stats(success):
    pygame.draw.rect(screen, BACKGROUND_COLOR, (440,40,500,100))
    global count
    global prob
    if success:
        count+=1
    else:
        count=0
        prob=1
    prob=prob*(1-count/100)
    font = pygame.font.SysFont('arial', 25)
    text=font.render('Level: '+str(count), True, WHITE)
    screen.blit(text, (450,50))
    text=font.render('Success rate: '+str(100-count)+'%', True, WHITE)
    screen.blit(text, (450,80))
    text=font.render('Probability: '+str(round(prob*100, 2))+'%', True, WHITE)
    screen.blit(text, (450,110))

def draw_progress_bar():
    global count
    pygame.draw.rect(screen, BACKGROUND_COLOR, (50,SCREEN_HEIGHT-80, 700, 30))
    pygame.draw.rect(screen, RED, (50,SCREEN_HEIGHT-80, count*7, 30))
    pygame.draw.rect(screen, WHITE, (50,SCREEN_HEIGHT-80,700,30),3)

def update_record():
    with open('best_score.txt', 'r') as f:
        max_count=f.read()
    max_count=int(max_count)
    if count>=max_count:
        pygame.draw.rect(screen, BACKGROUND_COLOR, (440,140,500,100))
        max_count=count
        max_prob=1
        for i in range(0, max_count):
            max_prob=max_prob*(1-max_count/100)

        font = pygame.font.SysFont('arial', 25)
        text=font.render('Level: '+str(max_count), True, WHITE)
        screen.blit(text, (450,150))
        text=font.render('Success rate: '+str(100-max_count)+'%', True, WHITE)
        screen.blit(text, (450,180))
        text=font.render('Probability: '+str(round(max_prob*100, 2))+'%', True, WHITE)
        screen.blit(text, (450,210))
        print(max_count)
        with open('best_score.txt', 'w') as f:
            f.write(str(max_count))



if __name__=='__main__':

    pygame.init()
    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
    pygame.display.set_caption('The button♥')
    font = pygame.font.SysFont('arial', 20)

    run  = True
    button=((50,350),(50,150))
    count=0
    prob=1

    draw_background()
    draw_button()
    update_stats(False)
    update_record()
    draw_progress_bar()



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