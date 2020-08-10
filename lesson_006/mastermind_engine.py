# -*- coding: utf-8 -*-

# Движок игры «Быки и коровы»
from random import randint
from termcolor import cprint, colored


def check_user_input():

    #  Александр, теперь, давайте немного поправим эту часть.
    #  1. Возвращать будет или False или список user_number_list (Список с Элементами всегда True). Так будет правильнее.
    #  2. Проверки осуществим с помощью одного условного оператора if/elif/else.
    #  Будем проверять "Количество неповторяющихся элементов в списке", "является ли числом", "начинается ли с нуля"
    #  И "количество символов".
    #  3. Тут же реализуем цикл while. Если пользователь ввёл некорректное число, повторяем цикл и просим ввести
    #  число заново. Если корректное - возвращаем число для выхода из цикла.
    # TODO сейчас реализовал в соответствии с третьим пунктом. Не совсем понимаю, как можно без цикла IF/ELSE в
    # основном модуле реализовать просьбу снова ввести число от пользователя. Сейчас число от пользователя я запрашиваю
    #   внутри функции check_user_input, при этом выполняя условие третей тудушки "Если пользователь ввёл некорректное " \
    # "число, повторяем цикл и просим ввести число заново." Но это расходится с принципом единственной ответственности.
    #   Может я не так понял этот пункт? Как мне попросить ввести число пользователя из функции, если запрос на введение
    # числа должен быть сделан из 01_mastermind?

    user_number_list = []
    while True:
        user_input = input(colored('Введите число : ', color='yellow'))
        for value in range(len(user_input)):
            user_number_list += [int(str(user_input)[value])]
        if len(user_input) != 4 or user_number_list[0] == 0 or len(user_number_list) != len(set(user_number_list)):
            cprint('Вы ввели неверное число! Число должно состоять из четырех неповторяющихся цифр и'
                   ' не должно начинаться с нуля.', color='red')
            user_number_list = []
            continue
        else:
            break
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
    # for i in range(4):
    #     if number_list[i] == user_number[i]:
    #         animals['bulls'] += 1
    #     elif number_list[i] in user_number:
    #         animals['cows'] += 1
    return animals
