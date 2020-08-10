# -*- coding: utf-8 -*-

# Движок игры «Быки и коровы»
from random import randint
from termcolor import cprint, colored


def check_user_input():
    while True:
        user_input = input(colored('Введите число : ', color='yellow'))
        user_number_list = list(map(int, user_input))
        if len(user_number_list) != 4:
            cprint('Вы ввели неверное число! Число должно состоять из четырех цифр.', color='red')
            continue
        elif user_number_list[0] == 0 or len(user_number_list) != len(user_number_list):
            cprint('Вы ввели неверное число! Число должно состоять из неповторяющихся цифр и'
                   ' не должно начинаться с нуля.', color='red')
            continue
        else:
            return user_number_list


number_list = []


def guess_the_number():
    global number_list
    number_list = []
    x = randint(1, 9)
    number_list += [x]
    while len(number_list) != 4:
        y = randint(0, 9)
        if y not in number_list:
            number_list += [y]
        else:
            continue
    return number_list


def check_the_number(user_number):
    animals = {'bulls': 0, 'cows': 0}
    for siting, value in enumerate(number_list):
        if value == user_number[siting]:
            animals['bulls'] += 1
        elif value in user_number:
            animals['cows'] += 1
    return animals
