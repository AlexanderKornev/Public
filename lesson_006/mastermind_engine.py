# -*- coding: utf-8 -*-

# Движок игры «Быки и коровы»
from random import randint

# TODO, Александр, давайте попробуем  немного сократить количество кода в 01_mastermind.py
#  В текущем модуле должно быть 3 функции.
#  1 - создать случайное число.
#  2 - проверка правильности введёного пользователем числа.
#  3 - подсчёт быков и коров.

# Есть две проблемы - при попытке начать новую игру,
# я пытаюсь вызвать снова функцию генерации числа, но она почему то возвращает тоже самое число.
# TODO, после того, первый раз, начиная игру мы берём пустую переменную number_list и заполняем её при условии
#  while len(number_list) != 4. len изначально == 0, потому всё "ок".
#  Когда начинаем второй раз игру, берётся переменная number_list. В которой уже есть данные и len = 4.
#  Потому, сразу идёт return number_list. Может пересоздавать её пустой до while? =)
number_list = []


# И еще один баг сейчас нашел. Когда я пробую начать новую игру с прежним числом функция проверки чисел на "быков/коров"
# выдает ошибку IndexError: list index out of range, хотя обычно работает без ошибок.
# TODO, После того, как пользователь ввёл "да" и число, в check_the_number передаётся пустой number_list = {list: 0} [].
#  Пожалуйста, попробуйте реализовать функцию для проверки введёного числа пользователем.
#  Количество кода и вложенных условных операторов if/else сократиться. Будет проще разобраться.



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
    animals = {'bulls': 0, 'cows': 0}

    # TODO, тут лучше идти по списку с enumerate number_list или user_number.
    #  Загаданное число предлагаю сделать глобальной переменной =)
    #  user_number=0000, наверное не стоит делать дефолтное значение. Пусть лучше будет парметр обязательным.
    #  Меньше багов будет =)
    for i in range(4):
        if number_list[i] == user_number[i]:
            animals['bulls'] += 1
        elif number_list[i] in user_number:
            animals['cows'] += 1
    return animals
