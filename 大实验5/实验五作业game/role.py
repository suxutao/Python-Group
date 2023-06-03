import pygame
import obstacle


class Role(pygame.sprite.Sprite):
    def __init__(self, jump_v=3, move_v=2, g=0.20):
        pygame.sprite.Sprite.__init__(self)
        self.role_size = [24, 24]
        self.picture_standing = pygame.transform.scale(pygame.image.load("picture\\person_standing.png")
                                                       .convert_alpha(), self.role_size)
        self.picture_left = pygame.transform.scale(pygame.image.load("picture\\person_left.png")
                                                   .convert_alpha(), self.role_size)
        self.picture_right = pygame.transform.scale(pygame.image.load("picture\\person_right.png")
                                                    .convert_alpha(), self.role_size)
        self.image = self.picture_standing
        self.rect = self.image.get_rect()
        self.jump_v = jump_v
        self.jump_now_v = 0
        self.jump_times = 0
        self.move_v = self.move_v_l = self.move_v_r = move_v
        self.down = False
        self.g = g
        self.font1 = self.font2 = None
        self.text1 = self.text2 = None
        self.max_jump_times = 2
        self.errors_v = 10
        self.errors_h = 3
        # the exact brick width is used here
        self.cmp_const_x = (self.rect.width + 25) / 2 - self.errors_h
        self.cmp_const_y = (self.rect.width + 25) / 2 - self.errors_v
        self.trap_tri = [False * 10]

    def move_right(self):
        if self.rect.left >= 1361:
            return
        self.rect.x += self.move_v_r
        self.image = self.picture_right

    def move_left(self):
        if self.rect.right <= 0:
            return
        self.rect.x -= self.move_v_l
        self.image = self.picture_left

    def drop(self):
        self.rect.y += self.jump_now_v
        self.jump_now_v += self.g

    def lose(self):
        self.font1 = pygame.font.SysFont("Times", 50)
        self.text1 = self.font1.render("dead", True, (255, 0, 0))
        self.font2 = pygame.font.SysFont("Times", 25)
        self.text2 = self.font2.render("input any key to retry", True, (255, 0, 0))

    def update(self, screen, *collide):
        key = pygame.key.get_pressed()
        # restore the initial value
        self.move_v_l = self.move_v_r = self.move_v
        self.down = True
        if collide[0]:
            for i in collide[0]:
                if self.rect.top < i.rect.top < self.rect.bottom and abs(self.rect.centerx - i.rect.centerx) < \
                        self.cmp_const_x:
                    if self.jump_now_v > 0:
                        self.jump_times = 0
                        self.jump_now_v = 0
                        self.rect.bottom = i.rect.top
                        self.down = False
                    # if self.jump_now_v > 10: // die of height
                    #     self.lose()
                elif self.rect.top < i.rect.bottom < self.rect.bottom and abs(self.rect.centerx -
                                                                              i.rect.centerx) < self.cmp_const_x:
                    if self.jump_now_v < 0:
                        self.jump_now_v = -self.jump_now_v

                elif self.rect.left < i.rect.left < self.rect.right and abs(self.rect.centery -
                                                                            i.rect.centery) < self.cmp_const_y:
                    self.move_v_r = 0
                elif self.rect.left < i.rect.right < self.rect.right and abs(self.rect.centery -
                                                                             i.rect.centery) < self.cmp_const_y:
                    self.move_v_l = 0
        if self.down:
            self.drop()
        if self.rect.top > 768:
            self.lose()
        if collide[1]:
            for i in collide[1]:
                if pygame.sprite.collide_mask(i, self):
                    self.lose()
        if key[pygame.K_LEFT]:
            self.move_left()
        elif key[pygame.K_RIGHT]:
            self.move_right()
        else:
            self.image = self.picture_standing
        screen.blit(self.image, self.rect)
