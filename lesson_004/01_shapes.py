# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# # В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

#
# def triangle(point, length, angle=0):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
#     v2.draw()
#
#     # v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
#     # v3.draw()
#     l3 = sd.line(start_point=v2.end_point, end_point=point, width=3)
#     print(l3)
#
#
# def square(point, length, angle=0):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle - 180, length=length, width=3)
#     v3.draw()
#
#     # v4 = sd.get_vector(start_point=v3.end_point, angle=angle - 90, length=lenght, width=3)
#     # v4.draw()
#
#     l5 = sd.line(start_point=v3.end_point, end_point=point, width=3)
#     print(l5)
#
#
# def pentagon(point, length, angle=0):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle - 72, length=length, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle - 144, length=length, width=3)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 144, length=length, width=3)
#     v4.draw()
#
#     # v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 72, length=lenght + 4, width=3)
#     # v5.draw()
#
#     l5 = sd.line(start_point=v4.end_point, end_point=point, width=3)
#     print(l5)
#
#
# def hexagon(point, length, angle=0):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
#     v4.draw()
#
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length + 4, width=3)
#     v5.draw()
#
#     # v6 = sd.get_vector(start_point=v5.end_point, angle=angle - 60, length=lenght + 4, width=3)
#     # v6.draw()
#
#     l6 = sd.line(start_point=v5.end_point, end_point=point, width=3)
#     print(l6)




# triangle(point, 100, 50)  # print наверное лишний =)
#
# point_square = sd.get_point(250, 250)
# square(point_square, 100, 40)
#
# point_pentagon = sd.get_point(400, 250)
# pentagon(point_pentagon, 100, 0)
#
# point_hexagon = sd.get_point(400, 400)
# hexagon(point_hexagon, 100, 0)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# зачёт первой части. Пожалуйста, приступайте ко второй!

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)


def vector(point, length, angle=0, lines=0):
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
            l3 = sd.line(start_point=v.end_point, end_point=begin_point, width=1)
            print(l3)


def triangle(point, length, angle):
    vector(point=point, angle=angle, length=length, lines=3)

def square(point, length, angle):
    vector(point=point, angle=angle, length=length, lines=4)

def pentagon(point, length, angle):
    vector(point=point, angle=angle, length=length, lines=5)

def hexagon(point, length, angle):
    vector(point=point, angle=angle, length=length, lines=6)


triangle_point = sd.get_point(100, 100)
triangle(point=triangle_point, length=100, angle=0)

point_square = sd.get_point(400, 100)
square(point=point_square, length=100, angle=0)

point_pentagon = sd.get_point(100, 400)
pentagon(point=point_pentagon, length=100, angle=0)

point_hexagon = sd.get_point(400, 400)
hexagon(point=point_hexagon, length=100, angle=0)

sd.pause()

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
