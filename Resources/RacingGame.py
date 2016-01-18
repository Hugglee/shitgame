import pygame
import time
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,480))
    
def menu(screen):
    pygame.display.set_caption("Menu")
    go = pygame.image.load("/home/ben/Desktop/Resources/go.png")
    quitt = pygame.image.load("/home/ben/Desktop/Resources/quit.png")
    screen.blit(go, (0,0))
    pygame.display.flip()
    while 1:
        checkforquit()
        mousepos = pygame.mouse.get_pos()
        if mousepos[1] < 240:
            screen.blit(go, (0,0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    main(screen)
        if mousepos[1] > 240:
            screen.blit(quitt, (0,0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    exit(0)
def checkforgameover1(playerpos, screen):
    wins2 = pygame.image.load("/home/ben/Desktop/Resources/2wins.png")
    if playerpos[0] < 515:
        if playerpos[0] > 75:
            if playerpos[1] > 75:
                if playerpos[1] < 355:
                    screen.blit(wins2,(0,0))
                    pygame.display.flip()
                    playerpos = [25,25]
                    time.sleep(3)
                    menu(screen)
def checkforgameover2(player2pos, screen):
    wins1 = pygame.image.load("/home/ben/Desktop/Resources/1wins.png")
    if player2pos[0] < 515:
        if player2pos[0] > 75:
            if player2pos[1] > 75:
                if player2pos[1] < 355:
                    screen.blit(wins1,(0,0))
                    pygame.display.flip()
                    player2pos = [310,240]
                    time.sleep(3)
                    menu(screen)
def checkforkeypress(keys,keys2):
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
        if event.type == pygame.KEYDOWN:
            if event.key==K_UP:
                keys2[0]=True
            elif event.key==K_LEFT:
                keys2[1]=True
            elif event.key==K_DOWN:
                keys2[2]=True
            elif event.key==K_RIGHT:
                keys2[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                keys2[0]=False
            elif event.key==pygame.K_LEFT:
                keys2[1]=False
            elif event.key==pygame.K_DOWN:
                keys2[2]=False
            elif event.key==pygame.K_RIGHT:
                keys2[3]=False
    return keys,keys2
def checkforquit(): #checks for if x is clicked
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
def main(screen):
    playerpos=[25,25]
    player2pos=[25,25]
    keys = [False, False, False, False]
    keys2 = [False, False, False, False]
    lap = 1
    lap2 = 1
    player = pygame.image.load("/home/ben/Desktop/Resources/tealcar.png")
    player2 = pygame.image.load("/home/ben/Desktop/Resources/yellowcar.png")
    track = pygame.image.load("/home/ben/Desktop/Resources/track.png")
    while 1:
        checkforquit()
        while 1:
            screen.blit(track, (0,0))
            screen.blit(player,playerpos)
            screen.blit(player2,player2pos)
            pygame.display.flip()
            checkforkeypress(keys,keys2)
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
            if keys2[0]:
                if player2pos[1] > 0:
                    player2pos[1] -= 3
            elif keys2[2]:
                if player2pos[1] < 430:
                    player2pos[1] += 3
            if keys2[1]:
                if player2pos[0] > 0:
                    player2pos[0] -= 3
                if player2pos[1] < 75:
                    if player2pos[0] == 320:
                        lap2 = lap2 - 1
                if player2pos[1] < 75:
                    if player2pos[0] == 321:
                        lap2 = lap2 - 1
                if player2pos[1] < 75:
                     if player2pos[0] == 322:
                        lap2 = lap2 - 1
            elif keys2[3]:
                if player2pos[0] < 590:
                    player2pos[0] += 3
                if player2pos[1] < 75:
                    if player2pos[0] == 320:
                        lap2 = lap2 + 1
                if player2pos[1] < 75:
                    if player2pos[0] == 321:
                        lap2 = lap2 + 1
                if player2pos[1] < 75:
                     if player2pos[0] == 322:
                        lap2 = lap2 + 1
            pygame.display.set_caption("Blue Laps: " + str(lap) + "                                                                                        Yellow Laps: " + str(lap2))
            checkforgameover1(playerpos, screen)
            checkforgameover2(player2pos, screen)
menu(screen)
main(screen)
