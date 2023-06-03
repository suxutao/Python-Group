"""
by Fu Ruoshan
May 10th, 2023
"""

import pygame
from obstacle import Bit, Brick
from background import Background
from role import Role
import random
import sys

brick_map1 = [[j * 25, 75] for j in range(20)]
brick_map1.extend([[525, j * 25] for j in range(25)])
brick_map1.extend([[450, 125 + i * 50] for i in range(10)])
brick_map1.extend([500, 125 + i * 50] for i in range(10))
brick_map1.extend([475, 125 + i * 50] for i in range(10))
brick_map1.extend([[25 * i, 625] for i in range(25)])

brick_map2 = [[650+50*i, 600-j*50] for i in range(10) for j in range(10)]

bit_map = [[450, i*100+50] for i in range(5)]
bit_map.append([1100, 100])
bit_map.extend([[25*i, 600] for i in range(20)])
bit_trap = [[0, 75], [0, 300]]


class Game(object):
    def __init__(self, fps: int, screen_size: ()):
        pygame.init()
        self.frame = fps
        self.fps = pygame.time.Clock()
        pygame.display.set_caption("difficult game by FURUOSHAN")
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode(screen_size)
        self.keep_going = True
        self.back = Background(1, screen_size)
        self.brick_group1 = pygame.sprite.Group()
        self.brick_group2 = pygame.sprite.Group()
        self.collide_with_brick = None
        self.collide_with_bit = None
        self.bit_group = pygame.sprite.Group()
        self.role = Role()
        self.pause = False
        self.trap_tri = [False]*10
        self.invincible = False
        self.end = None

    def update(self):
        self.screen.blit(self.back.image, self.back.rect)
        self.end = pygame.draw.circle(self.screen, (255, 255, 0), (1175, 150), 25)
        pygame.draw.circle(self.screen, (255, 0, 0), (1175, 150), 15)
        pygame.draw.circle(self.screen, (0, 0, 255), (1175, 150), 5)
        self.brick_group1.draw(self.screen)
        self.brick_group2.draw(self.screen)
        self.bit_group.update()
        self.bit_group.draw(self.screen)
        self.collide_with_brick = pygame.sprite.spritecollide(self.role, self.brick_group1, False)
        self.collide_with_brick.extend(pygame.sprite.spritecollide(self.role, self.brick_group2, False))
        for i in self.collide_with_brick:
            if i.rect.x >= 650:
                if not random.randint(0, 20):
                    for j in self.brick_group2:
                        if j.rect == i.rect:
                            self.brick_group2.remove(j)
        if not self.invincible:
            self.collide_with_bit = pygame.sprite.spritecollide(self.role, self.bit_group, False)
        self.role.update(self.screen, self.collide_with_brick, self.collide_with_bit)
        for i in self.bit_group:
            if 0 <= i.rect.x <= 1366 and 0 <= i.rect.y <= 768:
                continue
            self.bit_group.remove(i)
        pygame.display.update()

    def add_brick_group1(self, *sprite):
        pygame.sprite.Group.add(self.brick_group1, sprite)

    def add_brick_group2(self, *sprite):
        pygame.sprite.Group.add(self.brick_group2, sprite)

    def add_bit_group(self, *sprite):
        pygame.sprite.Group.add(self.bit_group, sprite)

    def creat_role(self, *pos):
        self.role.rect.x = pos[0]
        self.role.rect.y = pos[1]

    def trap(self):
        if self.role.rect.bottom > bit_trap[0][1]+5 and not self.trap_tri[0]:
            self.trap_tri[0] = True
            t = Bit(bit_trap[0][0], bit_trap[0][1], "bit_horizontal_left.png")
            t.speed_x = 100
            self.add_bit_group(t)
        if self.role.rect.bottom > bit_trap[1][1]+5 and not self.trap_tri[1]:
            self.trap_tri[1] = True
            t = Bit(bit_trap[1][0], bit_trap[1][1]+10, "bit_horizontal_left.png")
            t.speed_x = 100
            self.add_bit_group(t)
            for i in self.brick_group1:
                if i.rect.x == 525 and i.rect.y == 300:
                    self.brick_group1.remove(i)
                    break

    def if_win(self):
        if 1150 < self.role.rect.x < 1200 and 125 < self.role.rect.y < 175:
            return True
        return False

def init():
    game1 = Game(60, (1366, 768))
    game1.add_brick_group1(Brick(i[0], i[1]) for i in brick_map1)
    game1.add_brick_group2(Brick(i[0], i[1]) for i in brick_map2)
    game1.add_bit_group(Bit(i[0], i[1], "bit_horizontal_left.png") for i in bit_map)
    game1.creat_role(25, 25)
    pygame.mixer.music.load("music2/jump.wav")
    pygame.mixer.music.set_volume(0.2)
    return game1


game = init()
pygame.init()
flag = False
while game.keep_going:
        game.fps.tick(game.frame)
        game.trap()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                game.keep_going = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game.role.jump_times < game.role.max_jump_times:
                    game.role.jump_now_v = -game.role.jump_v
                    game.role.jump_times += 1
                    pygame.mixer.music.play()
        # invincible mode
        if pygame.key.get_pressed()[pygame.K_TAB]:
            game.invincible = True
        else:
            game.invincible = False
        game.update()
        if game.if_win():
            font1 = pygame.font.SysFont("Times", 50)
            text1 = font1.render("YOU WIN", True, (255, 0, 0))
            game.screen.blit(text1, game.role.rect)
            pygame.display.update()
            flag = True
        while flag:
                for event in pygame.event.get():
                    if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                        flag = False
                        game.keep_going = False
                        break
        if game.role.text1:
            if game.role.rect.left < 0:
                game.role.rect.left = 0
            if game.role.rect.right > 1100:
                game.role.rect.right = 1100
            if game.role.rect.top < 0:
                game.role.rect.top = 0
            if game.role.rect.bottom > 650:
                game.role.rect.bottom = 650
            game.screen.blit(game.role.text1, game.role.rect)
            game.screen.blit(game.role.text2, (game.role.rect.x, game.role.rect.y + 50))
            pygame.display.update()
            flag = True
        while flag:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        flag = False
                        game = init()
                        break
                    elif event.type == pygame.QUIT:
                        game.keep_going = False
                        flag = False
                        break
pygame.quit()
sys.exit()
