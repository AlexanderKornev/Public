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
            print(line_v)
            point = v.end_point
            angle = v.angle + next_angle
            shape_count = shape_count + 1
        else :
            l3 = sd.line(start_point=v.end_point, end_point=begin_point, width=1, color=color)
            print(l3)


def triangle(point, length, angle, color):
    vector(point=point, angle=angle, length=length, lines=3, color=color)

def square(point, length, angle, color):
    vector(point=point, angle=angle, length=length, lines=4, color=color)

def pentagon(point, length, angle, color):
    vector(point=point, angle=angle, length=length, lines=5, color=color)

def hexagon(point, length, angle, color):
    vector(point=point, angle=angle, length=length, lines=6, color=color)


color_dic = {'red': sd.COLOR_RED,
             'orange': sd.COLOR_ORANGE,
             'yellow': sd.COLOR_YELLOW,
             'green': sd.COLOR_GREEN,
             'cyan': sd.COLOR_CYAN,
             'blue': sd.COLOR_BLUE,
             'purple': sd.COLOR_PURPLE

             }

while True :
    user_color = input('Возможные цвета: ')
    for color in color_dic:
        if color == user_color:
            color = color_dic[color]
            triangle_point = sd.get_point(100, 100)
            triangle(point=triangle_point, length=100, angle=0, color=color)
            point_square = sd.get_point(400, 100)
            square(point=point_square, length=100, angle=0, color=color)
            point_pentagon = sd.get_point(100, 400)
            pentagon(point=point_pentagon, length=100, angle=0, color=color)
            point_hexagon = sd.get_point(400, 400)
            hexagosn(point=point_hexagon, length=100, angle=0, color=color)
            print(color)
        else:
            print('Вы ввели неккоретный номер!')
    if user_color in color_dic:
        break

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
