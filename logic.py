import random
import math
from main import input_digits


def create_number():
    num_digits = []
    loop = 0
    num = random.randint(10000, 99999)
    while loop < 5:
        num_digits.insert(0, math.floor(num % 10))
        num /= 10
        loop += 1
    return num_digits


def check_number(input_digits, num_digits):
    for i in range(len(input_digits)):
        if input_digits[i] in num_digits:
            if input_digits[i] != num_digits[i]:
                out_in[0] += 1
            if input_digits[i] == num_digits[i]:
                out_in[1] += 1
    return out_in
