'''
付文亮 2022080401004 欢迎界面设计
'''
import pygame
import sys
from pygame.locals import *
# 创建界面
pygame.init()
rect1 = None
rect2 = None
screen = pygame.display.set_mode(size=(1000,618),flags=0,depth=32)
title = pygame.image.load("sourse1/4.png").convert_alpha()
pygame.display.set_caption("1980年火爆游戏")
pygame.display.set_icon(title)
# 导入图片
picture1 = pygame.image.load("sourse1/1.png").convert_alpha()
Picture1 = pygame.transform.scale(picture1, (60, 60))
picture2 = pygame.image.load("sourse1/2.png").convert_alpha()
Picture2 = pygame.transform.scale(picture2, (80, 80))
picture = ["image1/1.png", "image1/2.png", "image1/3.png", "image1/4.png", "image1/5.png", "image1/6.png", "image1/7.png", "image1/8.png", "image1/9.png", "image1/10.png", "image1/11.png", "image1/12.png", "image1/13.png", "image1/14.png", "image1/15.png", "image1/16.png", "image1/17.png", "image1/18.png", "image1/19.png", "image1/20.png", "image1/21.png", "image1/22.png", "image1/23.png", "image1/24.png", "image1/25.png", "image1/26.png", "image1/27.png"]
picture0 = ["image2/1.png", "image2/2.png", "image2/3.png", "image2/4.png", "image2/5.png", "image2/6.png", "image2/7.png", "image2/8.png", "image2/9.png", "image2/10.png", "image2/11.png", "image2/12.png", "image2/13.png", "image2/14.png", "image2/15.png", "image2/16.png", "image2/17.png", "image2/18.png", "image2/19.png", "image2/20.png", "image2/21.png", "image2/22.png", "image2/23.png", "image2/24.png", "image2/25.png", "image2/26.png", "image2/27.png"]
picturelist0 = []
picturelist = []
# 调整图片尺寸
for n in picture:
    PICTURE = pygame.image.load(n).convert_alpha()
    Picture = pygame.transform.scale(PICTURE, (1000/2, 618))
    picturelist.append(Picture)
for n in picture0:
    PICTURE0 = pygame.image.load(n).convert_alpha()
    Picture0 = pygame.transform.scale(PICTURE0, (1000 / 2, 618))
    picturelist0.append(Picture0)
    # 效果显示与事件检测
while True:
    pygame.mixer.init()
    for event in pygame.event.get():
         if event.type == MOUSEMOTION:
             if 0 <=event.pos[0] and 500 >=event.pos[0] and event.pos[1]<=618 and event.pos[1]>=0:
                 pygame.mixer.music.load("music1/2.mp3")
                 pygame.mixer.music.play()
             if event.pos[0]>500 and event.pos[0]<=1000 and event.pos[1]<=618 and event.pos[1]>=0:
                 pygame.mixer.music.load("music1/3.mp3")
                 pygame.mixer.music.play()
         if event.type == QUIT:
             pygame.mixer.music.stop()
             pygame.quit()
             sys.exit()
         if event.type == pygame.MOUSEBUTTONDOWN and rect1 != None and rect2 != None:
             a = event.pos[0]
             b = event.pos[1]
             if rect1.collidepoint(a, b):  # 进入游戏1
                 pygame.mouse.set_visible(True)
                 pygame.mixer.music.stop()
                 from process import *
             if rect2.collidepoint(a, b):  # 进入游戏2
                 pygame.mouse.set_visible(True)
                 pygame.mixer.music.stop()
                 from game2 import *
        # 图像显示效果设置
    for i in range(27):
        screen.blit(picturelist[i], (1000/2, 0))
        screen.blit(picturelist0[i], (0, 0))
        rect1 = pygame.draw.rect(screen, (255, 255, 255), [1000 / 2 / 2 - 100, 618 / 2 - 20, 200, 40])
        rect2 = pygame.draw.rect(screen, (255, 255, 255), [(1000 / 2 + 1000 / 2 / 2) - 100, 618 / 2 - 20, 200, 40])
        rect3 = pygame.draw.rect(screen, (255, 255, 255), [1000 / 2, 0, 1, 618])
        font1 = pygame.font.SysFont('SimHei', 40)
        text1 = font1.render("怀旧马里奥", True, (255, 0, 0))
        font2 = pygame.font.SysFont('SimHei', 40)
        text2 = font2.render("小鸟向前冲", True, (0, 0, 0))
        font3 = pygame.font.SysFont('SimHei', 40)
        text3 = font3.render(chr(8599), True, (0, 0, 0))
        font4 = pygame.font.SysFont('SimHei', 40)
        text4 = font4.render(chr(8598), True, (255, 255, 255))
        font5 = pygame.font.SysFont('SimHei', 40)
        text5 = font5.render('点名称开始', True, (0, 0, 0))
        font6 = pygame.font.SysFont('SimHei', 40)
        text6 = font6.render('点名称开始', True, (255, 0, 0))
        screen.blit(text1, (1000 / 2 / 2 - 100, 618 / 2 - 20))
        screen.blit(text2, ((1000 / 2 + 1000 / 2 / 2) - 100, 618 / 2 - 20))
        screen.blit(text3, (1000 / 2 / 2 - 100+60, 618 / 2 - 20+40))
        screen.blit(text4, ((1000 / 2 + 1000 / 2 / 2) - 100+80, 618 / 2 - 20+40))
        screen.blit(text5, (1000 / 2 / 2 - 100, 618 / 2 - 20 + 40+40))
        screen.blit(text6, ((1000 / 2 + 1000 / 2 / 2) - 100, 618 / 2 - 20 + 40+40))
        if event.type == MOUSEMOTION:
            if 0 <= event.pos[0] and 500 >= event.pos[0] and event.pos[1] <= 618 and event.pos[1] >= 0:
                pygame.mouse.set_visible(True)
                screen.blit(Picture1, (event.pos[0], event.pos[1]))
            if event.pos[0] > 500 and event.pos[0] <= 1000 and event.pos[1] <= 618 and event.pos[1] >= 0:
                pygame.mouse.set_visible(True)
                screen.blit(Picture2, (event.pos[0], event.pos[1]))
        pygame.display.update()
        pygame.time.delay(33)
