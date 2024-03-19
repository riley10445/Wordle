import pygame
import logic
from sys import exit


class ShadowTile(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()
        self.image = pygame.Surface((90, 90))
        self.image.fill('black')
        self.rect = self.image.get_rect(topleft=coords)


class OutlineTile(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()
        self.image = pygame.Surface((90, 90))
        self.image.fill('gray48')
        self.rect = self.image.get_rect(topleft=coords)


class InputTile(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()
        self.image = pygame.Surface((86, 86))
        self.image.fill('gray20')
        self.rect = self.image.get_rect(topleft=coords)


class AnswerTile(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()
        self.image = pygame.Surface((86, 86))
        self.image.fill('#05350E')
        self.rect = self.image.get_rect(topleft=coords)


pygame.init()
pygame.display.set_caption('Numberdle')
screen = pygame.display.set_mode((550, 800))
screen.fill('gray20')
clock = pygame.time.Clock()
input_font = pygame.font.Font('Cabal-w5j3.ttf', 50)


shadow_wins = pygame.sprite.Group()
x_start_initial = 26
y_start = 17
for y in range(6):
    x_start = x_start_initial
    for x in range(5):
        shadow_wins.add(ShadowTile((x_start, y_start)))
        x_start += 100
    y_start += 120


outline_wins = pygame.sprite.Group()
x_start_initial = 30
y_start = 20
for y in range(6):
    x_start = x_start_initial
    for x in range(5):
        outline_wins.add(OutlineTile((x_start, y_start)))
        x_start += 100
    y_start += 120

input_wins = pygame.sprite.Group()
x_start_initial = 32
y_start = 22
for y in range(5):
    x_start = x_start_initial
    for x in range(5):
        input_wins.add(InputTile((x_start, y_start)))
        x_start += 100
    y_start += 120


answer_wins = pygame.sprite.Group()
x_start = 32
for x in range(5):
    input_wins.add(AnswerTile((x_start, 622)))
    x_start += 100


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    shadow_wins.draw(screen)
    outline_wins.draw(screen)
    input_wins.draw(screen)
    answer_wins.draw(screen)
    pygame.display.update()
    clock.tick(60)
