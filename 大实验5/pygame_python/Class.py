'''
Content:Classes and Methods
Author:苏徐涛
'''

import random
import math
import time
import pygame
from game import width,height

class Status:
    '''
    定义游戏状态
    '''
    def __init__(self):
        self.begin=False
        self.shift=False
        self.status=0  # 0表示游戏中，1表示胜利，2表示失败，3表示退出，4表示重开
        self.time=0
        self.music=1   # 1表示进程1，2表示进程2，3表示胜利，4表示失败，5表示重开
        self.Bird=0    #
        self.ctrl=False

class Bird:
    '''
    定义飞行的小鸟
    '''
    def __init__(self):
        self.birdStatus=[pygame.image.load('image/Bird.png').convert_alpha(),pygame.image.load('image/Bird.png').convert_alpha(),pygame.image.load('image/Bird.png').convert_alpha()]
        self.dead=False
        self.jump=False
        self.g=2
        self.a=10
        self.size=60
        self.x=width/2-self.size/2
        self.y=height/2-self.size/2
        self.score=0
        self.status=0
        self.birdRect=pygame.Rect(self.x+self.size/6,self.y+self.size/6,self.size*2/3,self.size*2/3)

    def up_down(self):
        if self.jump:
            self.a-=0.8
            self.y-=self.a
        else:
            self.g+=0.05
            self.y+=self.g
        self.birdRect[1]=self.y+self.size/6


class Pipeline:
    '''
    定义得分关键的管道,同时也是不同管道的基类
    '''
    def __init__(self):
        # 管道图片
        self.guandao_up=pygame.image.load('image/管道.png').convert_alpha()
        self.guandao_down=pygame.image.load('image/管道.png').convert_alpha()
        self.guankou_up=pygame.image.load('image/上管口.png').convert_alpha()
        self.guankou_down=pygame.image.load('image/下管口.png').convert_alpha()
        self.x=900
        self.v=5
        self.isappear=True
        self.size_guandao=self.guandao_up.get_height(),self.guandao_down.get_height()
        self.size_guankou=self.guankou_up.get_height()
        # 管道位置
        self.up_guandao=0
        self.up_guankou=self.size_guandao[0]
        self.down_guandao=height-self.size_guandao[1]
        self.down_guankou=self.down_guandao-self.size_guankou
        self.empty=(self.size_guankou+self.size_guandao[0],self.down_guankou)
        # 碰撞检测矩形
        self.guandao_up_Rect = pygame.Rect(self.x,self.up_guandao,self.guandao_up.get_width(),self.size_guandao[0])
        self.guandao_down_Rect = pygame.Rect(self.x,self.down_guandao,self.guandao_down.get_width(),self.size_guandao[1])
        self.guankou_up_Rect = pygame.Rect(self.x-12,self.up_guankou-5,self.guankou_up.get_width(),self.size_guankou-5)
        self.guankou_down_Rect = pygame.Rect(self.x-12,self.down_guankou+10,self.guankou_down.get_width(),self.size_guankou+10)

    def get_location(self):
        self.size_guandao = self.guandao_up.get_height(), self.guandao_down.get_height()
        self.size_guankou = self.guankou_up.get_height()
        # 管道位置
        self.up_guandao = 0
        self.up_guankou = self.size_guandao[0]
        self.down_guandao = height - self.size_guandao[1]
        self.down_guankou = self.down_guandao - self.size_guankou

    def appear(self):
        self.x-=self.v
        self.rect()
        if self.x<-80:
            self.x=900

    def rect(self):
        self.guandao_up_Rect = pygame.Rect(self.x, self.up_guandao, self.guandao_up.get_width(), self.size_guandao[0])
        self.guandao_down_Rect = pygame.Rect(self.x, self.down_guandao, self.guandao_down.get_width(),self.size_guandao[1])
        self.guankou_up_Rect = pygame.Rect(self.x - 12, self.up_guankou-5, self.guankou_up.get_width(), self.size_guankou-5)
        self.guankou_down_Rect = pygame.Rect(self.x - 12, self.down_guankou+10, self.guankou_down.get_width(),self.size_guankou+10)

    def disappear(self):
        self.x=1200
        self.v=0
        self.isappear=False

# 定义三种不同长度的管道
class Pipeline1(Pipeline):
    def __init__(self):
        Pipeline.__init__(self)
        self.transform()

    def transform(self):
        temp=random.randint(50,250)
        self.guandao_up = pygame.transform.scale(self.guandao_up, (self.guandao_up.get_width(), temp))
        self.guandao_down = pygame.transform.scale(self.guandao_down, (self.guandao_down.get_width(), 300-temp))
        self.get_location()
        self.empty = (self.size_guankou + self.size_guandao[0], self.down_guankou)

    def appear(self):
        self.x-=self.v
        self.rect()
        if self.x<-80:
            self.x=900
            self.transform()

class Pipeline2(Pipeline):
    def __init__(self):
        Pipeline.__init__(self)
        self.transform()

    def transform(self):
        temp=random.randint(50,250)
        self.guandao_up = pygame.transform.scale(self.guandao_up, (self.guandao_up.get_width(), temp))
        self.guandao_down = pygame.transform.scale(self.guandao_down, (self.guandao_down.get_width(), 350-temp))
        self.get_location()
        self.empty = (self.size_guankou + self.size_guandao[0], self.down_guankou)

    def appear(self):
        self.x-=self.v
        self.rect()
        if self.x<-80:
            self.x=900
            self.transform()

class Pipeline3(Pipeline):
    def __init__(self):
        Pipeline.__init__(self)
        self.transform()

    def transform(self):
        temp=random.randint(50,250)
        self.guandao_up = pygame.transform.scale(self.guandao_up, (self.guandao_up.get_width(), temp))
        self.guandao_down = pygame.transform.scale(self.guandao_down, (self.guandao_down.get_width(), 375-temp))
        self.get_location()
        self.empty = (self.size_guankou + self.size_guandao[0], self.down_guankou)

    def appear(self):
        self.x-=self.v
        self.rect()
        if self.x<-80:
            self.x=900
            self.transform()


class Monster:
    def __init__(self):
        self.v=7
        self.x=900
        self.y=random.randint(60,540)
        self.size=(60,60)
        self.music=pygame.mixer.Sound('music/jump.wav')  # 这个音乐是无效的，子类还会单独写各自的音乐
        self.music_trigger=False  # False代表未播放，True代表已经播放
        self.volume=0.3           # 初始音量
        self.coll=True            # 怪物的碰撞检测，默认开启检测
        self.image=True           # 怪物图片
        self.Rect = pygame.Rect(self.x - self.size[0] / 2.5, self.y - self.size[1] / 2.5, self.size[0] * 0.8,self.size[1] * 0.8)

    def appear(self,screen,empty:tuple):
        self.playmusic()
        self.x -= self.v
        screen.blit(self.image,(self.x - self.size[0] / 2, self.y - self.size[1] / 2))
        self.Rect = pygame.Rect(self.x - self.size[0] / 2.5, self.y - self.size[1] / 2.5, self.size[0] * 0.8,self.size[1] * 0.8)
        if self.x < -80:
            self.x=900
            self.y=random.randint(60,540)
            while self.y>empty[0] and self.y<empty[1]:
                self.y = random.randint(60, 540)
            self.music_trigger=False

    def disappear(self):
        self.x = 1200
        self.Rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.v = 0

    def playmusic(self):
        self.music.set_volume(self.volume)
        if not self.music_trigger:
            self.music_trigger=True
            self.music.play()

# 定义不同的怪物
class Dragon(Monster):
    '''恶龙类'''
    def __init__(self):
        Monster.__init__(self)
        self.music=pygame.mixer.Sound('music/dragon.aiff')
        self.v=-7
        self.size=(100,40)
        self.x=-self.size[0]
        self.time=time.time()
        self.image=[]
        for i in range(6):
            i=pygame.image.load(f'image/dragon{i+1}.png').convert_alpha()
            i=pygame.transform.scale(i,self.size)
            self.image.append(i)

    def appear(self,screen,empty:tuple):
        self.playmusic()
        self.x -= self.v
        Time=time.time()-self.time
        Time*=60;Time=int(Time);Time%=60
        screen.blit(self.image[Time//10], (self.x - self.size[0] / 2, self.y - self.size[1] / 2))
        self.Rect = pygame.Rect(self.x - self.size[0] / 2.5, self.y - self.size[1] / 2.5, self.size[0] * 0.8,self.size[1] * 0.8)
        if self.x > 900:
            self.x = -self.size[0]
            self.y = random.randint(40, 560)
            while self.y>empty[0] and self.y<empty[1]:
                self.y = random.randint(40, 560)
            self.music_trigger = False
            self.time=time.time()


class Shell(Monster):
    '''炮弹类'''
    def __init__(self):
        Monster.__init__(self)
        self.size=(60,40)
        self.image=pygame.image.load('image/shell.png').convert_alpha()
        self.image=pygame.transform.scale(self.image, self.size)
        self.music=pygame.mixer.Sound('music/shell.wav')
        self.Rect = pygame.Rect(self.x - self.size[0] / 2.5, self.y - self.size[1] / 2.5, self.size[0] * 0.8,self.size[1] * 0.8)


class Ghost(Monster):
    '''幽灵类'''
    def __init__(self):
        Monster.__init__(self)
        self.image=pygame.image.load('image/ghost.png').convert_alpha()
        self.image=pygame.transform.scale(self.image, self.size)
        self.music=pygame.mixer.Sound('music/ghost.mp3')
        self.volume=0.5
        self.x=random.randint(600,850)
        self.y=random.randint(60,540)
        self.waiting_time=-1

    def draw_ellipse(self,screen):
        color=[random.randint(100,255) for i in range(3)]
        rect=[self.x-20,self.y-40,40,80]
        pygame.draw.ellipse(screen,color,rect)

    def appear(self,screen,empty:tuple):
        # 幽灵出现
        if self.waiting_time == -1:
            self.waiting_time = time.time()
        if time.time() - self.waiting_time < 2:
            self.draw_ellipse(screen)
        elif self.x>-80:
            self.coll = True
            self.playmusic()
            screen.blit(self.image, (self.x - self.size[0] / 2, self.y - self.size[1] / 2))
            self.Rect = pygame.Rect(self.x - self.size[0] / 2.5, self.y - self.size[1] / 2.5, self.size[0] * 0.8,self.size[1] * 0.8)
            self.x -= self.v
        else:
            self.coll = False
            self.waiting_time=-1
            self.x = random.randint(600, 850)
            self.y = random.randint(60, 540)
            while self.y>empty[0] and self.y<empty[1]:
                self.y = random.randint(60, 540)
            self.music_trigger=False


class Star(Monster):
    '''星星类'''
    def __init__(self):
        Monster.__init__(self)
        self.v=0
        self.x=450
        self.image=pygame.image.load('image/star.png').convert_alpha()
        self.image=pygame.transform.scale(self.image, self.size)
        self.music=pygame.mixer.Sound('music/star.mp3')
        self.y=random.randint(60,540)
        self.waiting_time=-1   # 星星出现前的等待时间
        self.coll=False

    def draw_star(self,screen):
        # 在怪物正式出现之前，先画一个五角星，此时不进行碰撞检测
        color = [random.randint(100, 255) for i in range(3)]
        x1 = [self.x + 35 * math.sin(0.4 * math.pi * i) for i in range(5)]
        x2 = [self.x + 15 * math.sin(0.4 * math.pi * i + math.pi / 5) for i in range(5)]
        y1 = [self.y - 35 * math.cos(0.4 * math.pi * i) for i in range(5)]
        y2 = [self.y - 15 * math.cos(0.4 * math.pi * i + math.pi / 5) for i in range(5)]
        points = []
        for i in range(10):
            if i % 2 == 0:
                points.append((x1[i // 2], y1[i // 2]))
            else:
                points.append((x2[i // 2], y2[i // 2]))
        pygame.draw.polygon(screen, color, points, 3)

    def appear(self,screen,empty:tuple):
        # 星星出现
        if self.waiting_time==-1:
            self.waiting_time=time.time()
        if time.time()-self.waiting_time<1:
            pass
        elif time.time()-self.waiting_time<3 and time.time()-self.waiting_time>1:
            self.draw_star(screen)
        elif time.time()-self.waiting_time<4.5:
            self.coll=True
            self.playmusic()
            screen.blit(self.image, (self.x - self.size[0] / 2, self.y - self.size[1] / 2))
            self.Rect = pygame.Rect(self.x - self.size[0] / 2.5, self.y - self.size[1] / 2.5, self.size[0]*0.8, self.size[1]*0.8)
        else:
            self.y=random.randint(60,540)
            while self.y>empty[0] and self.y<empty[1]:
                self.y = random.randint(60, 540)
            self.waiting_time=-1
            self.music_trigger=False
            self.coll=False