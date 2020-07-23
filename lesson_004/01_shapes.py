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

point = sd.get_point(100, 100)
def triangle(point, lenght, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=lenght, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=lenght, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=lenght, width=3)
    v3.draw()

print(triangle(point, 100, 50))

point_square = sd.get_point(250, 250)
def square(point, lenght, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=lenght, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=lenght, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle - 180, length=lenght, width=3)
    v3.draw()

    # v4 = sd.get_vector(start_point=v3.end_point, angle=angle - 90, length=lenght, width=3)
    # v4.draw()

    l5 = sd.line(start_point=v3.end_point, end_point=point, width=3)
    print(l5)

square(point_square, 100, 40)

point_pentagon = sd.get_point(400, 250)
def pentagon(point, lenght, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=lenght, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle - 72, length=lenght, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle - 144, length=lenght, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 144, length=lenght, width=3)
    v4.draw()

    # v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 72, length=lenght + 4, width=3)
    # v5.draw()

    l5 = sd.line(start_point=v4.end_point, end_point=point, width=3)
    print(l5)

pentagon(point_pentagon, 100, 0)


point_hexagon = sd.get_point(400, 400)
def hexagon(point, lenght, angle=0) :
    v1 = sd.get_vector(start_point=point, angle=angle, length=lenght, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=lenght, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=lenght, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=lenght, width=3)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=lenght + 4, width=3)
    v5.draw()

    # v6 = sd.get_vector(start_point=v5.end_point, angle=angle - 60, length=lenght + 4, width=3)
    # v6.draw()

    l6 = sd.line(start_point=v5.end_point, end_point=point, width=3)
    print(l6)


hexagon(point_hexagon, 100, 0)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

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

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()