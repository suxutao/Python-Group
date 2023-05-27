'''
Content:Flying Bird Game
Author:苏徐涛
'''

import sys
import time
from Class import *
import pygame

# 窗口大小
width=900;height=600
size=(width,height)
chang=600;gao=300
da_xiao=(chang,gao)

def UpdateMap():
    '''
    展示小鸟、管道、怪物、背景
    '''
    # 三个阶段
    if Bird.score//10==0 or Pipeline1.isappear:
        screen.blit(background1,(0,0))

        # 显示上管道
        screen.blit(Pipeline1.guandao_up, (Pipeline1.x, Pipeline1.up_guandao))
        screen.blit(Pipeline1.guankou_up, (Pipeline1.x - 12, Pipeline1.up_guankou))
        # 显示下管道
        screen.blit(Pipeline1.guandao_down, (Pipeline1.x, Pipeline1.down_guandao))
        screen.blit(Pipeline1.guankou_down, (Pipeline1.x - 12, Pipeline1.down_guankou))
        Pipeline1.appear()

        if Pipeline1.x == Bird.x:
            Bird.score += 1

    elif Bird.score//10==1 or Pipeline2.isappear:
        screen.blit(background2,(0,0))

        # 显示上管道
        screen.blit(Pipeline2.guandao_up, (Pipeline2.x, Pipeline2.up_guandao))
        screen.blit(Pipeline2.guankou_up, (Pipeline2.x - 12, Pipeline2.up_guankou))
        # 显示下管道
        screen.blit(Pipeline2.guandao_down, (Pipeline2.x, Pipeline2.down_guandao))
        screen.blit(Pipeline2.guankou_down, (Pipeline2.x - 12, Pipeline2.down_guankou))
        Pipeline2.appear()

        if Pipeline2.x == Bird.x:
            Bird.score += 1

    elif Bird.score//10==2:
        if Bird.score==20 and Status.music!=-2:
            Status.music=2
            music()
        screen.blit(background3,(0,0))
        # 显示上管道
        screen.blit(Pipeline3.guandao_up, (Pipeline3.x, Pipeline3.up_guandao))
        screen.blit(Pipeline3.guankou_up, (Pipeline3.x - 12, Pipeline3.up_guankou))
        # 显示下管道
        screen.blit(Pipeline3.guandao_down, (Pipeline3.x, Pipeline3.down_guandao))
        screen.blit(Pipeline3.guankou_down, (Pipeline3.x - 12, Pipeline3.down_guankou))
        Pipeline3.appear()

        if Pipeline3.x == Bird.x and Bird.score >= 28:
            Bird.score += 0.5
        elif Pipeline3.x == Bird.x:
            Bird.score += 1

    # 显示怪物
    if Bird.score>5:
        Shell1.appear(screen,Pipeline1.empty)
        if Bird.score>10:
            Shell2.appear(screen,Pipeline2.empty)
            if Bird.score>15:
                Shell2.disappear()
                Dragon.appear(screen,Pipeline2.empty)
                if Bird.score>20:
                    Ghost.appear(screen,Pipeline3.empty)
                    if Bird.score>22:
                        Star.appear(screen,Pipeline3.empty)
    # 公布得分和时间
    screen.blit(time_text,(0,0))
    screen.blit(score_text,(0,50))

    if Bird.score==10 and Pipeline1.x<=-80:
        Pipeline1.disappear()
    if Bird.score==20 and Pipeline2.x<=-80:
        Pipeline2.disappear()

    if Bird.dead:
        Bird.status=2
    elif Bird.jump:
        Bird.status=1

    Status.Bird=(Bird.x,Bird.y)
    screen.blit(Image_bird,Status.Bird)
    Bird.up_down()

def CheckDead():
    '''
    检测小鸟是否死亡
    '''
    if Bird.y < -40 or Bird.y > 600:
        Bird.dead = True
    if Status.ctrl:
        return 0
    # 检测怪物
    Rect=Shell1.Rect,Shell2.Rect,Dragon.Rect,Ghost.Rect,Star.Rect
    for i in range(len(Rect)):
        if Bird.birdRect.colliderect(Rect[i]) and i<3:
            Bird.dead=True
        if Bird.birdRect.colliderect(Rect[i]) and i==3 and Ghost.coll==True:
            Bird.dead=True
        if Bird.birdRect.colliderect(Rect[i]) and i==4 and Star.coll==True:
            Bird.dead=True
    # 检测管道
    rect=Pipeline1.guandao_up_Rect,Pipeline1.guankou_up_Rect,Pipeline1.guandao_down_Rect,Pipeline1.guankou_down_Rect,Pipeline2.guandao_up_Rect,Pipeline2.guankou_up_Rect,Pipeline2.guandao_down_Rect,Pipeline2.guankou_down_Rect,Pipeline3.guandao_up_Rect,Pipeline3.guankou_up_Rect,Pipeline3.guandao_down_Rect,Pipeline3.guankou_down_Rect
    for i in range(len(rect)):
        if Bird.birdRect.colliderect(rect[i]):
            Bird.dead=True
    # 小鸟死亡后换遗像
    if Bird.dead==True:
        screen.blit(Image_bird_dead, Status.Bird)

def music():
    if Status.music == 1:
        Status.music = -1
        music_begin.stop()
        music_pos1.set_volume(0.3)
        music_pos1.play()
    elif Status.music == 2:
        Status.music = -2
        music_pos1.stop()
        music_pos2.set_volume(0.3)
        music_pos2.play()
    elif Status.music == 3:
        Status.music = -3
        music_pos2.stop()
        music_victory.set_volume(0.3)
        music_victory.play()
    elif Status.music == 4:
        Status.music = -4
        music_pos1.stop()
        music_pos2.stop()
        music_failure.set_volume(0.3)
        music_failure.play()
    elif Status.music == 5:
        Status.music=1
        music_failure.stop()
        music_victory.stop()


if __name__ == '__main__':

    # 初始化设置，窗口大小，标题，图标展示
    pygame.init()
    screen=pygame.display.set_mode(size)
    pygame.display.set_caption('Flying Bird!')
    ico=pygame.image.load('image/Bird_ico.png')
    pygame.display.set_icon(ico)
    clock=pygame.time.Clock()

    # 类的初始化
    Status=Status()
    Bird=Bird()
    Pipeline1=Pipeline1()
    Pipeline2=Pipeline2()
    Pipeline3=Pipeline3()
    Dragon=Dragon()
    Shell1=Shell()
    Shell2=Shell()
    Ghost=Ghost()
    Star=Star()

    # 背景图片
    background1=pygame.image.load('image/background1.png').convert_alpha()
    background1=pygame.transform.scale(background1,size)
    background2 = pygame.image.load('image/background2.png').convert_alpha()
    background2 = pygame.transform.scale(background2, size)
    background3 = pygame.image.load('image/background3.png').convert_alpha()
    background3 = pygame.transform.scale(background3, size)

    # 鸟的图片
    bird_size=Bird.size
    Image_bird=pygame.image.load('image/Bird.png').convert_alpha()
    Image_bird=pygame.transform.scale(Image_bird,(bird_size,bird_size))
    Image_bird_dead=pygame.image.load('image/DeadBird.png').convert_alpha()
    Image_bird_dead=pygame.transform.scale(Image_bird_dead,(bird_size,bird_size))

    # 音乐
    channel=pygame.mixer.find_channel(True)
    channel_jump=pygame.mixer.find_channel(True)
    channel_jump.set_volume(0.2)
    music_begin=pygame.mixer.Sound('music/助手.mp3')
    music_pos1=pygame.mixer.Sound('music/询问2.mp3')
    music_pos2=pygame.mixer.Sound('music/询问2+.mp3')
    music_victory=pygame.mixer.Sound('music/胜诉3.mp3')
    music_failure=pygame.mixer.Sound('music/真相的苦涩味.mp3')
    music_jump=pygame.mixer.Sound('music/jump.wav')
    channel.play(music_begin)

    # 字体和文本
    start_font=pygame.font.SysFont('微软雅黑', 60)
    start_text=start_font.render('Click to start!', True, 'blue')
    info_font=pygame.font.SysFont('黑体',30)
    info_text=info_font.render('''按鼠标或空格键进行跳跃,按shift键进行冲刺''',True,'darkblue')
    score_font=pygame.font.SysFont('微软雅黑',50)
    time_font = pygame.font.SysFont('微软雅黑', 50)
    settle_font=pygame.font.SysFont('幼圆',60)
    settle_font2=pygame.font.SysFont('微软雅黑',40)
    choice_font=pygame.font.SysFont('华文行楷',60)

    # 游戏主体
    while 1:
        clock.tick(60)
        if Status.status==4:
            # 重新开始
            Status.__init__()
            Bird.__init__()
            Pipeline1.__init__()
            Pipeline2.__init__()
            Pipeline3.__init__()
            Ghost.__init__()
            Shell1.__init__()
            Shell2.__init__()
            Star.__init__()
            Dragon.__init__()
            music_victory.stop()
            music_failure.stop()
            channel.set_volume(0.3)
            channel.play(music_begin)
            continue
        if Bird.dead:
            time.sleep(1)
            Status.status=2
        if Bird.score==30:
            if Status.music == -2:
                Status.music=3
                music()
            Status.status=1
            time.sleep(0.5)
        # 键盘，鼠标轮询
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN and not Status.begin:
                Status.music=1
                music()
                Status.begin = 1
                start_time=time.time()
            if (event.type ==pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE) and not Bird.dead and Status.begin:
                Bird.jump=True
                Bird.g=2
                Bird.a=10
                music_jump.set_volume(0.3)
                music_jump.play()
            if event.type==pygame.KEYDOWN and (event.key==pygame.K_LSHIFT or event.key==pygame.K_RSHIFT):
                Status.shift=True
            if event.type==pygame.KEYUP and (event.key==pygame.K_LSHIFT or event.key==pygame.K_RSHIFT):
                Status.shift=False
            if event.type==pygame.KEYDOWN and (event.key==pygame.K_LCTRL or event.key==pygame.K_RCTRL):
                Status.ctrl=True
            if event.type==pygame.KEYUP and (event.key==pygame.K_LCTRL or event.key==pygame.K_RCTRL):
                Status.ctrl=False
            if event.type==pygame.MOUSEBUTTONDOWN and Status.status in (1,2):
                mouse_x,mouse_y=event.pos
                if mouse_x > width / 2 - chang / 2+50 and mouse_x<width / 2 - chang / 2+290 and mouse_y>350 and mouse_y<410:
                    Status.status=4
                if mouse_x > width / 2 - chang / 2+350 and mouse_x<width / 2 - chang / 2+590 and mouse_y>350 and mouse_y<410:
                    pygame.quit()
                    sys.exit()

        # 按shift实现冲刺，按ctrl实现无敌
        if Status.shift:
            Pipeline1.v = 10
            Pipeline2.v = 10
            Pipeline3.v = 10
            Ghost.v = 12
            Shell1.v = 12
            Shell2.v = 12
            Dragon.v = -2
        else:
            Pipeline1.v = 5
            Pipeline2.v = 5
            Pipeline3.v = 5
            Ghost.v = 7
            Shell1.v = 7
            Shell2.v = 7
            Dragon.v = -7

        # 其他事件
        if Status.status==0:
            if Status.begin:
                score_text = score_font.render(f'得分：{Bird.score}', True, 'purple')
                Status.time=time.time()-start_time
                time_text = time_font.render('时间：%.2f' % (Status.time), True, 'blue')
                UpdateMap()
                CheckDead()
            else:
                screen.blit(background1,(0,0))
                screen.blit(start_text, (250, 130))
                screen.blit(info_text,(0,570))
                screen.blit(Image_bird, (width / 2 - bird_size / 2, height / 2 - bird_size / 2))
        elif Status.status==1:
            settle_text1 = settle_font.render('恭喜你，游戏成功! ', True, 'magenta')
            settle_text2 = settle_font2.render('得分：%d      用时：%.2f' % (Bird.score, Status.time), True, 'red')
            choice_text1 = choice_font.render('重新开始', True, '#0066ff', 'pink')
            choice_text2 = choice_font.render('退出游戏', True, '#0066ff', 'pink')
            screen.blit(settle_text1, (width / 2 - chang / 2 + 60, height / 2 - gao / 2))
            screen.blit(settle_text2, (width / 2 - chang / 2 + 100, height / 2 - gao / 2 + 100))
            screen.blit(choice_text1, (width / 2 - chang / 2 + 50, 350))
            screen.blit(choice_text2, (width / 2 - chang / 2 + 350, 350))
        elif Status.status==2:
            if Status.music in (-1,-2) and Status.music!=-4:
                Status.music=4
                music()
            settle_text1 = settle_font.render('很遗憾，游戏失败! ', True, 'black')
            settle_text2 = settle_font2.render('得分：%d      用时：%.2f' % (Bird.score, Status.time), True, 'darkblue')
            choice_text1=choice_font.render('重新开始',True,'#000033','#99ff99')
            choice_text2=choice_font.render('退出游戏',True,'#000033','#99ff99')
            screen.blit(settle_text1, (width / 2 - chang / 2+60, height / 2 - gao / 2))
            screen.blit(settle_text2, (width / 2 - chang / 2+100, height / 2 - gao / 2 + 100))
            screen.blit(choice_text1, (width / 2 - chang / 2+50,350))
            screen.blit(choice_text2, (width / 2 - chang / 2+350,350))

        pygame.display.flip()
