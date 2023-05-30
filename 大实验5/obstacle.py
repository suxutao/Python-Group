import pygame


class Brick(pygame.sprite.Sprite):
    def __init__(self, left: int, up: int):
        pygame.sprite.Sprite.__init__(self)
        self.brick_size = [25, 25]
        self.image = pygame.transform.scale(pygame.image.load("picture/brick2.png"), self.brick_size).convert()
        self.rect = self.image.get_rect()
        self.rect.x = left
        self.rect.y = up


class Bit(pygame.sprite.Sprite):
    def __init__(self, left: int, up: int, picture: str):
        pygame.sprite.Sprite.__init__(self)
        self.bit_size = [25, 25]
        self.image = pygame.transform.scale(pygame.image.load(f"picture/{picture}"), self.bit_size).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = left
        self.rect.y = up
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
