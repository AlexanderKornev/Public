# -*- coding: utf-8 -*-

# Движок игры «Быки и коровы»
from random import randint
from termcolor import cprint


def check_user_input(user_input):

    # TODO, Александр, теперь, давайте немного поправим эту часть.
    #  1. Возвращать будет или False или список user_number_list (Список с Элементами всегда True). Так будет правильнее.
    #  2. Проверки осуществим с помощью одного условного оператора if/elif/else.
    #  Будем проверять "Количество неповторяющихся элементов в списке", "является ли числом", "начинается ли с нуля"
    #  И "количество символов".
    #  3. Тут же реализуем цикл while. Если пользователь ввёл некорректное число, повторяем цикл и просим ввести
    #  число заново. Если корректное - возвращаем число для выхода из цикла.

    user_number_list = []
    if len(user_input) != 4:
        return 1, cprint('Вы ввели число не из четырех символов или вообще не число!', color='red')
    if len(user_input) == 4:
        for value in range(4) :
            user_number_list += [int(str(user_input)[value])]
        if user_number_list[0] == 0 or len(user_number_list) != len(set(user_number_list)):
            return 1, cprint('Вы ввели неверное число! Число не должно начинаться с нуля или содержать '
                             'повторяющиеся цифры.', color='red')
        else:
            print(user_number_list)
    return 0, user_number_list


number_list = []
def guess_the_number():
    global number_list
    number_list= []
    # TODO, эту часть тоже можно упростить. Пожалуйста, подумайте как =)
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


def check_the_number(user_number):
    animals = {'bulls': 0, 'cows': 0}
    for siting, value in enumerate(number_list):
        if value == user_number[siting]:
            animals['bulls'] += 1
        elif value in user_number:
            animals['cows'] += 1
    # for i in range(4):
    #     if number_list[i] == user_number[i]:
    #         animals['bulls'] += 1
    #     elif number_list[i] in user_number:
    #         animals['cows'] += 1
    return animals
