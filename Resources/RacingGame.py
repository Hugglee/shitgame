import pygame
import time
from pygame.locals import *
def checkforkeypress(keys):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False
    return keys
def checkforquit(): #checks for if x is clicked
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
def main():
    #declare all the variables
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    playerpos=[25,25]
    keys = [False, False, False, False]
    lap = 1
    alive = 0
    gameover = 0
    player = pygame.image.load("/home/ben/Desktop/Resources/tealcar.png")
    track = pygame.image.load("/home/ben/Desktop/Resources/track.png")
    gameover = pygame.image.load("/home/ben/Desktop/Resources/gameover.png")
    #start of loop
    while 1:
        checkforquit()
        while (alive == 0):
            screen.blit(track, (0,0))
            screen.blit(player,playerpos)
            pygame.display.flip()
            checkforkeypress(keys)
            if keys[0]:
                if playerpos[1] > 0:
                    playerpos[1] -= 3
            elif keys[2]:
                if playerpos[1] < 430:
                    playerpos[1] += 3
            if keys[1]:
                if playerpos[0] > 0:
                    playerpos[0] -= 3
                if playerpos[1] < 75:
                    if playerpos[0] == 320:
                        lap = lap - 1
                if playerpos[1] < 75:
                    if playerpos[0] == 321:
                        lap = lap - 1
                if playerpos[1] < 75:
                     if playerpos[0] == 322:
                        lap = lap - 1
            elif keys[3]:
                if playerpos[0] < 590:
                    playerpos[0] += 3
                if playerpos[1] < 75:
                    if playerpos[0] == 320:
                        lap = lap + 1
                if playerpos[1] < 75:
                    if playerpos[0] == 321:
                        lap = lap + 1
                if playerpos[1] < 75:
                     if playerpos[0] == 322:
                        lap = lap + 1
            pygame.display.set_caption("Laps: " + str(lap))
            if playerpos[0] < 515:
                if playerpos[0] > 75:
                    if playerpos[1] > 75:
                        if playerpos[1] < 355:
                            screen.blit(gameover,(0,0))
                            pygame.display.flip()
                            playerpos = [25,25]
                            lap = 1
                            time.sleep(1)
main()
