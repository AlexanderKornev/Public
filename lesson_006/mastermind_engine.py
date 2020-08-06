# -*- coding: utf-8 -*-

# Движок игры «Быки и коровы»
from random import randint

number_list = []
def guess_the_number():
    global number_list
    while len(number_list) != 4:
        if len(number_list) < 1:
            x = randint(1, 9)
            number_list += [x]
        y = randint(0, 9)
        if y not in number_list:
            number_list += [y]
        else:
            continue
    return number_list


def check_the_number(number_list, user_number=0000):

    animals = {'bulls' : 0, 'cows' : 0}

    for i in range(4):
        if number_list[i] == user_number[i]:
            animals['bulls'] += 1
        elif number_list[i] in user_number:
            animals['cows'] += 1
    return animals

