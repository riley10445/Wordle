import pygame
import random
from math import floor
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


class GreenTile(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()
        self.image = pygame.Surface((86, 86))
        self.image.fill('springgreen3')
        self.rect = self.image.get_rect(topleft=coords)


class YellowTile(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()
        self.image = pygame.Surface((86, 86))
        self.image.fill('yellow3')
        self.rect = self.image.get_rect(topleft=coords)


def load_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()  # Read words into a list, removing any trailing newline characters
    return words


def draw_previous(previous):
    base = [50, 35]
    for row_index, answer in enumerate(previous):
        for letter_index, letter in enumerate(answer):
            answer_surface = font.render(letter, True, 'black')
            screen.blit(answer_surface, (base[0]+(letter_index*100), base[1]+(row_index*120)))


def draw_correct(correct):
    correct = correct.upper()
    base = [50, 635]
    for num in range(5):
        answer_surface = font.render(correct[num], True, 'white')
        screen.blit(answer_surface, (base[0]+(num*100), base[1]))

green_wins = pygame.sprite.Group()
yellow_wins = pygame.sprite.Group()
def create_colored_tiles(itemized_list):
    base = [32, 22]
    for num in range(len(itemized_list)):
        row = floor(num/5)
        column = num % 5
        if itemized_list[num] == 1:
            yellow_wins.add(YellowTile((base[0]+(column*100), base[1]+(row*120))))
        if itemized_list[num] == 2:
            green_wins.add(GreenTile((base[0]+(column*100), base[1]+(row*120))))


def check_input(word_input, correct, item_list):
    word_lower = word_input.lower()
    for num in range(5):
        if word_lower[num] in correct:
            if word_lower[num] != correct[num]:
                item_list.append(1)
            elif word_lower[num] == correct[num]:
                item_list.append(2)
        else:
            item_list.append(0)


pygame.init()
pygame.display.set_caption('Numberdle')
screen = pygame.display.set_mode((550, 800))
screen.fill('gray20')
clock = pygame.time.Clock()
font = pygame.font.Font('Swansea-q3pd.ttf', 70)


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
base_position = [50, 35]
row_num = 1
previous_answers = []
itemized_values = []

file_path = 'sgb-words.txt'
words = load_words(file_path)
correct_word = random.choice(words)
print(correct_word)

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
            elif len(typed) < 5:
                if event.unicode.isalpha():
                    typed += event.unicode.upper()
            elif len(typed) == 5 and event.key == pygame.K_RETURN:
                if typed.lower() not in words or typed in previous_answers:
                    typed = ''
                else:
                    previous_answers.append(typed)
                    check_input(typed, correct_word, itemized_values)
                    typed = ''
                    row_num += 1
                    base_position[0] = 50
                    base_position[1] += 120
    if row_num == 6:
        draw_correct(correct_word)
    create_colored_tiles(itemized_values)
    yellow_wins.draw(screen)
    green_wins.draw(screen)
    draw_previous(previous_answers)
    for i, char in enumerate(typed):
        text_surface = font.render(char, True, 'black')
        screen.blit(text_surface, (base_position[0] + (i * 100), base_position[1]))
    pygame.display.update()
    clock.tick(60)
