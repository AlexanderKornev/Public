# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1200, 1000)
# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

snowflake_dict = {}  # Словарь со снежинками для отрисовки
quantity_snowflakes = 30


def create_snowflakes(quantity_snowflakes=10):
    global snowflake_dict
    for number_x in range(quantity_snowflakes):
        x = sd.random_number(100, 1100)
        y = sd.random_number(700, 800)
        length = sd.random_number(5, 30)
        snowflake_dict[number_x] = [x, y, length]
    return snowflake_dict


def snowflakes_color(color):
    for sf_name, value in snowflake_dict.items():
        x = value[0]
        y = value[1]
        length = value[2]
        point = sd.get_point(x, y)
        sd.snowflake(center=point, length=length, color=color)


def move_snowflakes():
    for sf_name, value in snowflake_dict.items():
        value[0] += sd.random_number(-5, 5)
        value[1] -= sd.random_number(5, 20)
        point2 = sd.get_point(value[0], value[1])
        sd.snowflake(center=point2, length=value[2], color=sd.COLOR_CYAN)


bottom_screen_list = []  # список для удаления снежинок.


def bottom_screen():
    global bottom_screen_list
    for sf_name, value in snowflake_dict.items():
        if value[1] < 10:
            bottom_screen_list += [sf_name]  # Заполняем ключами упавших снежинок? Почему при y < 400?
    return bottom_screen_list




def delete_and_creat_snowflake():
    global bottom_screen_list, snowflake_dict
    for delete_number in bottom_screen_list:
        snowflake_dict.pop(delete_number, None)
        x = sd.random_number(100, 1100)
        y = sd.random_number(700, 850)
        length = sd.random_number(5, 30)
        snowflake_dict[delete_number + 10] = [x, y, length]
    bottom_screen_list = []
    return snowflake_dict, bottom_screen_list

