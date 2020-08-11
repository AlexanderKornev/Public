# -*- coding: utf-8 -*-

import simple_draw as sd

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
from lesson_006.snowfall import create_snowflakes, snowflakes_color, move_snowflakes, \
    bottom_screen, delete_and_creat_snowflake

# TODO Можно упростить импорт
#  import lesson_006.snowfall as sn
#  Как в таком случае будет происходить вызов функции?




create_snowflakes()
while True:
    snowflakes_color(color=sd.background_color)
    move_snowflakes()
    snowflakes_color(color=sd.COLOR_CYAN)
    bottom_screen_fn = bottom_screen()
    if len(bottom_screen_fn) > 0:
        delete_and_creat_snowflake()
        continue
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
