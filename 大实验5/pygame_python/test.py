import sys
import math
from Class import *
import pygame


pygame.init()
screen=pygame.display.set_mode((900,600))
Star=Star()
Ghost=Ghost()
Shell=Shell()
Dragon=Dragon()
a=1
x=450;y=300
clock=pygame.time.Clock()
while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('cyan')
    screen.blit(Star.image, (0, 0))
    # points = [(200, 50), (250, 150), (350, 150), (275, 225), (325, 350), (200, 275), (75, 350), (125, 225),
    #           (50, 150), (150, 150)]
    # pygame.draw.polygon(screen, (255, 255, 0), points)
    color = [random.randint(100, 255) for i in range(3)]
    x1 = [x+40*math.sin(0.4*math.pi*i) for i in range(5)]
    x2 = [x+15*math.sin(0.4*math.pi*i+math.pi/5) for i in range(5)]
    y1 = [y-40*math.cos(0.4*math.pi*i) for i in range(5)]
    y2 = [y-15*math.cos(0.4*math.pi*i+math.pi/5) for i in range(5)]
    points=[]
    for i in range(10):
        if i%2==0:
            points.append((x1[i//2],y1[i//2]))
        else:
            points.append((x2[i//2],y2[i//2]))
    pygame.draw.polygon(screen, color, points,2)
    # Ghost.playmusic()
    # Shell.playmusic()
    # Star.playmusic()
    # Star.appear(screen)
    # Ghost.appear(screen)
    # Shell.appear(screen)
    Dragon.appear(screen)
    pygame.display.flip()