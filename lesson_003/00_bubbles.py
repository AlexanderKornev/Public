# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(300, 300)
# radius = 50
# for _ in range(3):
#     radius += 5
#     sd.circle(center_position=point, radius=radius, width=2)

# #
# # Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def bubble(point, step, color):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=2)


point = sd.get_point(300, 300)
bubble(point=point, step=20, color=sd.COLOR_BLACK)
#
# Нарисовать 10 пузырьков в ряд
for x in range(100, 1001, 100):
    point = sd.get_point(x, 100)
    # TODO, Александр, пожалуйста, обратите внимание, код не запускается
    #  TypeError: bubble() missing 1 required positional argument: 'color',
    #  означает, что функция ждёт аргумент color, так как он не задан по умолчани.
    bubble(point=point, step=5)
#
# # # Нарисовать три ряда по 10 пузырьков
for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        # TODO, В этом месте тоже. Давайте поправим.
        bubble(point=point, step=5)
#
# # # Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# for _ in range(100):
#     point = sd.random_point()
#     color = sd.random_color()
#     bubble(point=point, step=6, color=color)

sd.pause()
