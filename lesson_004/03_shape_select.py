# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def vector(point, length, angle=0, lines=0, color=sd.COLOR_RED):
    begin_point = point
    next_angle = 360 // lines
    shape_count = 0
    shape_for_line = lines - 1
    for _ in range(lines):
        if shape_count < shape_for_line:
            v = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
            v.draw()
            point = v.end_point
            angle = v.angle + next_angle
            shape_count = shape_count + 1
        else:
            sd.line(start_point=v.end_point, end_point=begin_point, width=1, color=color)


def triangle(point, length, angle):
    vector(point=point, angle=angle, length=length, lines=3)


def square(point, length, angle):
    vector(point=point, angle=angle, length=length, lines=4)


def pentagon(point, length, angle):
    vector(point=point, angle=angle, length=length, lines=5)


def hexagon(point, length, angle):
    vector(point=point, angle=angle, length=length, lines=6)


figure_dic = {
    '0': ['треугольник', triangle],
    '1': ['квадрат', square],
    '2': ['пятиугольник', pentagon],
    '3': ['шестиугольник', hexagon]
}


while True:
    print('Фигуры: ')
    for number, figure_print in figure_dic.items():
        figure_name = figure_dic[number][0]
        print(number, ':', figure_name)
    user_figure = input('Введите желаемую фигуру: ')
    if user_figure in figure_dic:
        figure = figure_dic[user_figure][1]
        point = sd.get_point(300, 300)
        figure(point, 100, 0)
        break
    else:
        print('Вы ввели некорректный номер!')


sd.pause()
