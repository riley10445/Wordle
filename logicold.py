import random
import math


def create_number():
    num_digits = []
    loop = 0
    num = random.randint(10000, 99999)
    while loop < 5:
        num_digits.insert(0, math.floor(num % 10))
        num /= 10
        loop += 1
    return num_digits


def input_number():
    input_num = int(input("Guess a number: "))
    input_digits = []
    loop = 0
    while loop < 5:
        input_digits.insert(0, math.floor(input_num % 10))
        input_num /= 10
        loop += 1
    return input_digits


def check_number(input_digits, num_digits):
    out_of_place = in_place = 0
    for i in range(len(input_digits)):
        if input_digits[i] in num_digits:
            if input_digits[i] != num_digits[i]:
                out_of_place += 1
            if input_digits[i] == num_digits[i]:
                in_place += 1
    print(f"There are {out_of_place} digits in the incorrect position.\n")
    print(f"There are {in_place} correct digits.\n")
