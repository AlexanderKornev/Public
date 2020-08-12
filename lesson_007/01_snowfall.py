# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = 1800, 900


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake :
    snowflake_cords = []
    # snowflake_list = []

    def __init__(self, name=None) :
        self.name = name
        return

    def __str__(self) :
        return self

    def create(self) :
        x = sd.random_number(100, 1100)
        y = sd.random_number(700, 800)
        length = sd.random_number(5, 30)
        Snowflake.snowflake_cords = [x, y, length]
        return Snowflake.snowflake_cords

    def move(self) :
        Snowflake.snowflake_cords[0] += sd.random_number(-5, 5)
        Snowflake.snowflake_cords[1] -= sd.random_number(5, 20)
        return Snowflake.snowflake_cords

    def clear_previous_picture(self) :
        x = Snowflake.snowflake_cords[0]
        y = Snowflake.snowflake_cords[1]
        length = Snowflake.snowflake_cords[2]
        point = sd.get_point(x, y)
        sd.snowflake(center=point, length=length, color=sd.background_color)

    def draw(self) :
        x = Snowflake.snowflake_cords[0]
        y = Snowflake.snowflake_cords[1]
        length = Snowflake.snowflake_cords[2]
        point = sd.get_point(x, y)
        sd.snowflake(center=point, length=length)

    def can_fall(self) :
        if Snowflake.snowflake_cords[1] > 10 :
            return True
        else :
            return False


    # def get_flakes(self, count):
    #     name: int
    #     for name in range(count):
    #         Snowflake.snowflake_list += [Snowflake(self=name)]
    #         for name2 in Snowflake.snowflake_list:
    #             Snowflake(name2).create()
    #
    #     return Snowflake.snowflake_list

flake = Snowflake()
flake.create()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


# class Blizzard:
#
#     snowflake_list = []
#
#     def __init__(self) :
#         self.count = None
#
#     def get_flakes(self, count) :
#         self.count = count
#         for name in range(self.count) :
#             Blizzard.snowflake_list = [Snowflake(name)]
#         return Blizzard.snowflake_list
#
#
#
#
# # шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flake = Blizzard()
# flakes = flake.get_flakes(10) # создать список снежинок
# while True:
#     for create in flakes:
#         Snowflake().create()
#         break
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     # fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     # if fallen_flakes:
#     #     append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
#
# sd.pause()
