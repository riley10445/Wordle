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


def draw_previous(previous):
    base = [55, 22]
    for row_index, answer in enumerate(previous):
        for letter_index, letter in enumerate(answer):
            answer_surface = font.render(letter, True, 'white')
            screen.blit(answer_surface, (base[0] + (letter_index * 100), base[1] + (row_index * 120)))


pygame.init()
pygame.display.set_caption('Numberdle')
screen = pygame.display.set_mode((550, 800))
screen.fill('gray20')
clock = pygame.time.Clock()
font = pygame.font.Font('Cabal-w5j3.ttf', 70)


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

typed = ''
base_position = [55, 22]
row_num = 1
previous_answers = []


while True:
    shadow_wins.draw(screen)
    outline_wins.draw(screen)
    input_wins.draw(screen)
    answer_wins.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and row_num < 6:
            if event.key == pygame.K_BACKSPACE:
                typed = typed[:-1]
                print(typed)
            elif len(typed) < 5:
                if event.unicode.isprintable():
                    typed += event.unicode.upper()
                    print(typed)
            elif len(typed) == 5 and event.key == pygame.K_RETURN:
                previous_answers.append(typed)
                typed = ''
                row_num += 1
                base_position[0] = 55
                base_position[1] += 120
    draw_previous(previous_answers)
    for i, char in enumerate(typed):
        text_surface = font.render(char, True, 'white')
        screen.blit(text_surface, (base_position[0] + (i * 100), base_position[1]))
    pygame.display.update()
    clock.tick(60)
