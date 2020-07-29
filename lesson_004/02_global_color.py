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
    for _ in range(lines-1):
        v = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
        v.draw()
        sd.line(start_point=v.start_point, end_point=v.end_point, width=1, color=color)
        point = v.end_point
        angle = v.angle + next_angle
    sd.line(start_point=v.end_point, end_point=begin_point, width=1, color=color)


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
    '0': ['red', sd.COLOR_RED],
    '1': ['orange', sd.COLOR_ORANGE],
    '2': ['yellow', sd.COLOR_YELLOW],
    '3': ['green', sd.COLOR_GREEN],
    '4': ['cyan', sd.COLOR_CYAN],
    '5': ['blue', sd.COLOR_BLUE],
    '6': ['purple', sd.COLOR_PURPLE],
}


while True:
    for number_color, number_name_color in color_dic.items():
        color_name = number_name_color[0]
        print(number_color, ':', color_name)
    user_color = input('Введите желаемый цвет: ')
    # TODO, Александр, давайте немного упростим проверку. Будем проверять, есть ли в словаре user_color ключ,
    #  который ввёл пользователь. В таком случае, приводить ответ пользователя к int будет не нужно.
    #  Проверять > 6, тоже необходимость отпадёт. Если такой ключ в словаре есть, создаём переменную с цветом
    #  и выходим из цикла.
    #  Фигуры отрисуем уже вне цикла. В остально код рабочий! Молодец!
    if int(user_color) > 6:
        print('Вы ввели некорректный номер!')
    else:
        color = color_dic[user_color][1]
        triangle_point = sd.get_point(100, 100)
        triangle(point=triangle_point, length=100, angle=0, color=color)
        point_square = sd.get_point(400, 100)
        square(point=point_square, length=100, angle=0, color=color)
        point_pentagon = sd.get_point(100, 400)
        pentagon(point=point_pentagon, length=100, angle=0, color=color)
        point_hexagon = sd.get_point(400, 400)
        hexagon(point=point_hexagon, length=100, angle=0, color=color)
        break
    # elif 6 > user_color < 0:
    #     print('Вы ввели некорректный номер!')

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
