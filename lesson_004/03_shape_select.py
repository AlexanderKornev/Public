# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def vector(point, length, angle=0, lines=0, color=sd.COLOR_RED) :
    begin_point = point
    next_angle = 360 // lines
    shape_count = 0
    shape_for_line = lines - 1
    for _ in range(lines) :
        if shape_count < shape_for_line :
            v = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
            v.draw()
            line_v = sd.line(start_point=v.start_point, end_point=v.end_point, width=1, color=color)
            point = v.end_point
            angle = v.angle + next_angle
            shape_count = shape_count + 1
        else :
            l3 = sd.line(start_point=v.end_point, end_point=begin_point, width=1, color=color)


def triangle(point, length, angle):
    vector(point=point, angle=angle, length=length, lines=3)

def square(point, length, angle):
    vector(point=point, angle=angle, length=length, lines=4)

def pentagon(point, length, angle):
    vector(point=point, angle=angle, length=length, lines=5)

def hexagon(point, length, angle):
    vector(point=point, angle=angle, length=length, lines=6)

# TODO Пожалуйста, произведите перенос текста, как я сделал это в 02.
#  В этом месте тоже, лучше использовать в виде ключей ожидаемую от пользователя цифру в строковом формате.
figure_dic = {'треугольник': 3,
             'квадрат': 4,
             'пятиугольник': 5,
             'шестиугольник': 6
             }

while True :
    print('Фигуры: ')
    for number, figure_print in enumerate(figure_dic):
        print(number, ':', figure_print)
    user_figure = int(input('Введите желаемую фигуру: '))
    if user_figure < 4:
        for figure_number, lines in enumerate(figure_dic):
            if figure_number == user_figure:
                lines = figure_dic[lines]
                # TODO, тоже лучше вынести за пределы цикла отрисовку фигуры и оставить
                #  только создание переменной фигурой.
                center = sd.get_point(200, 200)
                vector(point=center, length=100, angle=0, lines=lines, color=sd.COLOR_RED)
        break
    elif user_figure > 4:
        print('Вы ввели некорректный номер!')










sd.pause()