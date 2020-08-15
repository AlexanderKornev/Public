# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = 1800, 900


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self, name=None):
        self.name = name
        self.x = sd.random_number(100, 1100)
        self.y = sd.random_number(700, 800)
        self.length = sd.random_number(5, 30)

    def __str__(self):
        return self

    def move(self):
        self.x += sd.random_number(-5, 5)
        self.y -= sd.random_number(5, 20)

    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=sd.background_color)

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length)

    def can_fall(self):
        return self.y > 10


snowflake_list = []


def get_flakes(count):
    global snowflake_list
    for name in range(count):
        snowflake_list.append(Snowflake())
    return snowflake_list


def get_fallen_flakes():
    for_remove = []
    count = 0
    for i in snowflake_list:
        if i.can_fall() is False:
            count += 1
            for_remove.append(i)
    return count, for_remove


def remove(for_remove_list):
    global snowflake_list
    for i in for_remove_list:
        snowflake_list.remove(i)
    return snowflake_list


# flake = Snowflake()
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# # шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:

flakes = get_flakes(10)  # создать список снежинок

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        get_flakes(count=fallen_flakes[0])  # добавить еще сверху
        remove(for_remove_list=fallen_flakes[1])
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# зачёт!
