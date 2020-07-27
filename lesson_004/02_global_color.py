# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

def vector(point, length, angle=0, lines=0, color=sd.COLOR_RED):
    begin_point = point
    next_angle = 360 // lines
    shape_count = 0
    shape_for_line = lines - 1
    for _ in range(lines):
        if shape_count < shape_for_line:
            v = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
            v.draw()
            # TODO, line как переменную создавать не нужно =) она всегда рисуется сразу.
            line_v = sd.line(start_point=v.start_point, end_point=v.end_point, width=1, color=color)
            point = v.end_point
            angle = v.angle + next_angle
            shape_count = shape_count + 1
        else:
            # TODO, line как переменную создавать не нужно =) она всегда рисуется сразу.
            l3 = sd.line(start_point=v.end_point, end_point=begin_point, width=1, color=color)


def triangle(point, length, angle, color):
    vector(point=point, angle=angle, length=length, lines=3, color=color)


def square(point, length, angle, color):
    vector(point=point, angle=angle, length=length, lines=4, color=color)


def pentagon(point, length, angle, color):
    vector(point=point, angle=angle, length=length, lines=5, color=color)


def hexagon(point, length, angle, color):
    vector(point=point, angle=angle, length=length, lines=6, color=color)


# Пожалуйста, обратите внимание на перенос текста.
color_dic = {
    'red': sd.COLOR_RED,
    'orange': sd.COLOR_ORANGE,
    'yellow': sd.COLOR_YELLOW,
    'green': sd.COLOR_GREEN,
    'cyan': sd.COLOR_CYAN,
    'blue': sd.COLOR_BLUE,
    'purple': sd.COLOR_PURPLE
}

# TODO, Александр, пожалуйста. Обратите внимание. Т.к. мы используем словарь.
#  Ответ пользователя приводить к int не нужно. Лучше, ключами в словаре использовать числа в формате строки,
#  которые может ввести пользователь. ("0", "1" и т.д.) В таком случае название цвета и сам цвет будут как значения.
#  Их можно объеденить в список или в ещё один словарь. Получится Словарь списков или словарь словарей =).
while True:
    print('Возможные цвета: ')
    for number, color_print in enumerate(color_dic):
        print(number, ':', color_print)
    user_color = int(input('Введите желаемый цвет: '))
    if 0 < user_color < 6:
        for color_number, color_color in enumerate(color_dic):
            if color_number == user_color:
                #  TODO, получилось много вложенных циклов и условий. После реализации первой части ТУДУ
                #   они должны уйти =) Предлагаю оставить переменную color в цикле while,
                #   а отрисовку делать уже после, когда перменная создана.
                color = color_dic[color_color]
                triangle_point = sd.get_point(100, 100)
                triangle(point=triangle_point, length=100, angle=0, color=color)
                point_square = sd.get_point(400, 100)
                square(point=point_square, length=100, angle=0, color=color)
                point_pentagon = sd.get_point(100, 400)
                pentagon(point=point_pentagon, length=100, angle=0, color=color)
                point_hexagon = sd.get_point(400, 400)
                hexagon(point=point_hexagon, length=100, angle=0, color=color)
        break
    elif 6 > user_color < 0:
        print('Вы ввели некорректный номер!')

# triangle_point = sd.get_point(100, 100)
# triangle(point=triangle_point, length=100, angle=0)
#
# point_square = sd.get_point(400, 100)
# square(point=point_square, length=100, angle=0)
#
# point_pentagon = sd.get_point(100, 400)
# pentagon(point=point_pentagon, length=100, angle=0)
#
# point_hexagon = sd.get_point(400, 400)
# hexagon(point=point_hexagon, length=100, angle=0)


sd.pause()
