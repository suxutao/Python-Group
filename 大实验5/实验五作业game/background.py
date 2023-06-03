import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, move_v: int, screen_size: ()):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("picture/background.png"), screen_size).convert()
        self.rect = self.image.get_rect()
        self.ground = 100
        self.move_v = move_v

    def move_left(self):
        self.rect.x -= self.move_v

    def move_right(self):
        self.rect.x += self.move_v

    def update_move_v(self, move_v: int):
        self.move_v = move_v
