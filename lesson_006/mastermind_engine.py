# -*- coding: utf-8 -*-

# Движок игры «Быки и коровы»
from random import randint
from termcolor import cprint, colored

# TODO, Александр, давайте попробуем  немного сократить количество кода в 01_mastermind.py
#  В текущем модуле должно быть 3 функции.
#  1 - создать случайное число.
#  2 - проверка правильности введёного пользователем числа.
#  3 - подсчёт быков и коров.

def check_user_input(user_input):
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


# check_user_input(user_input)
# Есть две проблемы - при попытке начать новую игру,
# я пытаюсь вызвать снова функцию генерации числа, но она почему то возвращает тоже самое число.
# TODO, после того, первый раз, начиная игру мы берём пустую переменную number_list и заполняем её при условии
#  while len(number_list) != 4. len изначально == 0, потому всё "ок".
#  Когда начинаем второй раз игру, берётся переменная number_list. В которой уже есть данные и len = 4.
#  Потому, сразу идёт return number_list. Может пересоздавать её пустой до while? =)



# И еще один баг сейчас нашел. Когда я пробую начать новую игру с прежним числом функция проверки чисел на "быков/коров"
# выдает ошибку IndexError: list index out of range, хотя обычно работает без ошибок.
# TODO, После того, как пользователь ввёл "да" и число, в check_the_number передаётся пустой number_list = {list: 0} [].
#  Пожалуйста, попробуйте реализовать функцию для проверки введёного числа пользователем.
#  Количество кода и вложенных условных операторов if/else сократиться. Будет проще разобраться.


number_list = []
def guess_the_number():
    global number_list
    number_list= []
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
    # TODO, тут лучше идти по списку с enumerate number_list или user_number.
    #  Загаданное число предлагаю сделать глобальной переменной =)
    #  user_number=0000, наверное не стоит делать дефолтное значение. Пусть лучше будет парметр обязательным.
    #  Меньше багов будет =)
    # for i in range(4):
    #     if number_list[i] == user_number[i]:
    #         animals['bulls'] += 1
    #     elif number_list[i] in user_number:
    #         animals['cows'] += 1
    return animals
