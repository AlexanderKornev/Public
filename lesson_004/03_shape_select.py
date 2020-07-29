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
            line_v = sd.line(start_point=v.start_point, end_point=v.end_point, width=1, color=color)
            point = v.end_point
            angle = v.angle + next_angle
            shape_count = shape_count + 1
        else:
            l3 = sd.line(start_point=v.end_point, end_point=begin_point, width=1, color=color)


def triangle(point, length, angle):
    vector(point=point, angle=angle, length=length, lines=3)


def square(point, length, angle):
    vector(point=point, angle=angle, length=length, lines=4)


def pentagon(point, length, angle):
    vector(point=point, angle=angle, length=length, lines=5)


def hexagon(point, length, angle):
    vector(point=point, angle=angle, length=length, lines=6)

# TODO, Александр, пожалуйста, обратите внимание, как можно зранить функции в словаре и как вызывать их.
#  example_figure_dic = {
#      '0': ['треугольник', triangle],
#  }
#  example_func = example_figure_dic["0"][1]  # Создаём функцию
#  example_func()  # Вызываем функцию

# TODO, пожалуйста переделайте этот словарь =)
figure_dic = {
    '0': ['треугольник', 3],
    '1': ['квадрат', 4],
    '2': ['пятиугольник', 5],
    '3': ['шестиугольник', 6]
}

while True:
    print('Фигуры: ')
    for number, figure_print in figure_dic.items():
        figure_name = figure_dic[number][0]
        print(number, ':', figure_name)
    user_figure = input('Введите желаемую фигуру: ')
    # TODO, Александр, давайте в этом месте так же проверять. Является ли то,
    #  что ввёл пользователь ключём нашего словаря. Если да, то создаём функцию. Вызываем её уже вне цикла.
    #  Цикл нужен только для проерки введёного пользователем и создания функции.
    if int(user_figure) > 3:
        print('Вы ввели некорректный номер!')
    else:
        lines = figure_dic[user_figure][1]
        center = sd.get_point(200, 200)
        vector(point=center, length=100, angle=0, lines=lines, color=sd.COLOR_RED)
        break

sd.pause()
