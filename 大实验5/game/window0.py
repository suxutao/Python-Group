import pygame
import sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode(size=(1000,618),flags=0,depth=32)
title = pygame.image.load("sourse1/3.png").convert_alpha()
pygame.display.set_caption("时光机")
pygame.display.set_icon(title)
picture = pygame.image.load("sourse1/5.png").convert_alpha()
Picture = pygame.transform.scale(picture, (1000, 618))
word1 = pygame.font.SysFont('SimHei', 80)
text1 = word1.render("点击开始穿越旅行", True, (0, 0, 0))
pygame.mixer.init()
pygame.mixer.music.load("music1/4.mp3")
pygame.mixer.music.play()
while True:
    screen.blit(Picture, (0, 0))
    rect1 = pygame.draw.rect(screen, (255, 255, 255), (1000 / 2 - 240-80, 618 / 2 + 50, 640, 80))
    screen.blit(text1, (1000/2-240-80, 618/2+50))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect1.collidepoint(event.pos[0], event.pos[1]):
                pygame.mixer.music.stop()
                from window1 import *