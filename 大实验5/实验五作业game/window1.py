'''
付文亮 2022080401004 欢迎界面设计
'''
import pygame
import sys
from pygame.locals import *
# 创建界面
pygame.init()
screen = pygame.display.set_mode(size=(1000,618),flags=0,depth=32)
title = pygame.image.load("sourse1/3.png").convert_alpha()
pygame.display.set_caption("传送仓")
pygame.display.set_icon(title)
# 导入图片
picturelist = []
picture = ["image3/1.png", "image3/2.png", "image3/3.png", "image3/4.png", "image3/5.png", "image3/6.png", "image3/7.png", "image3/8.png", "image3/9.png", "image3/10.png", "image3/11.png", "image3/12.png", "image3/13.png", "image3/14.png", "image3/15.png", "image3/16.png", "image3/17.png", "image3/18.png", "image3/19.png", "image3/20.png", "image3/21.png", "image3/22.png", "image3/23.png", "image3/24.png", "image3/25.png", "image3/26.png", "image3/27.png", "image3/28.png", "image3/29.png", "image3/30.png", "image3/31.png", "image3/32.png", "image3/33.png", "image3/34.png", "image3/35.png", "image3/36.png", "image3/37.png", "image3/38.png", "image3/39.png", "image3/40.png", "image3/41.png", "image3/42.png", "image3/43.png", "image3/44.png", "image3/45.png", "image3/46.png", "image3/47.png", "image3/48.png", "image3/49.png"]
# 调整图片尺寸
for n in picture:
    Picture = pygame.image.load(n).convert_alpha()
    PICTURE = pygame.transform.scale(Picture, (1000,618))
    picturelist.append(PICTURE)
while True:
    pygame.mixer.init()
    pygame.mixer.music.load("music1/1.mp3")
    pygame.mixer.music.play()
    # 显示操作
    for i in range(49):
        screen.blit(picturelist[i], (0,0))
        rect1=pygame.draw.rect(screen, (0, 0, 0), (1000/2-440,618/2-80,880,80))
        word1 = pygame.font.SysFont('SimHei', 80)
        text1 = word1.render("正在穿越中，请稍等片刻", True, (255, 255, 255))
        screen.blit(text1, (1000/2-440, 618/2-80))
        pygame.display.update()
        pygame.time.delay(50)
        if i == 48 :
            pygame.mixer.music.stop()
            # 进入下一板块
            from window2 import *
    # 退出系统
    for event in pygame.event.get():
        pygame.mixer.music.stop()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()