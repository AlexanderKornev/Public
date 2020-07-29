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

def vector(point, length, color=sd.COLOR_YELLOW, lines=0):
    #  Просто если убрать sd.line внутри цикла
    # не будет разных цветов, и параметр color не нужен т.к. sd.get_vector не имеет значения color.
    # TODO, 1. если рисовать следом line, получается двойная работа. =)
    #  2. sd.get_vector не имеет параметра color. Но при отрисовке созданного вектора v.draw(),
    #  можно указать параметр color =)


    # А вы в предыдущем ТУДУ предложили поиграть с цветами.
    begin_point = point
    next_angle = 360 // lines
    # А ещё, тут сделать range от 0, до 360 не включительно с шагом next_angle.
    # И next_angle использовать как угол для отрисовки. Для треугольника он будет 0, 120, 240.
    #   таком лучае, вычисления angle = v.angle + next_angle будут лишними.
    for angle in range(0, 360, next_angle):
        # TODO, если треугольник, то надо отрисовать 2 стороны с помощью вектора.
        #  Сейчас рисуем 3 стороны т.к. angle => 0, 120, 240. next_angle = 120
        #  нам надо отрисовать 2 стороны т.е. angle толжен быть => 0, 120. На сколько надо сократить 360 в range?
        x = next_angle * (lines - 1)  # лишний код
        if x == angle: # лишний код
            break  # лишний код
        #  добавил range по angle. К сожалению, в таком случае не удается "затормозить" цикл на предпоследней
        #  линии. Он рисует ВСЕ векторы=линиям, а последнюю с неправильным углом.
        #  Поэтому добавил условие по разрыву цикала.
        # TODO, чуть Выше указал, как можно поступить, чтобы не писать лишний код =)
        v = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
        v.draw()
        # sd.line(start_point=v.start_point, end_point=v.end_point, color=color, width=5)
        point = v.end_point
    sd.line(start_point=v.end_point, end_point=begin_point, width=2, color=sd.COLOR_GREEN)


def triangle(point, length, color):
    vector(point=point, color=color, length=length, lines=3)


def square(point, length, color):
    vector(point=point, color=color, length=length, lines=4)


def pentagon(point, length, color):
    vector(point=point, color=color, length=length, lines=5)


def hexagon(point, length, color):
    vector(point=point, color=color, length=length, lines=6)


triangle_point = sd.get_point(100, 100)
triangle(point=triangle_point, length=100, color=sd.random_color())

point_square = sd.get_point(400, 100)
square(point=point_square, length=100, color=sd.random_color())

point_pentagon = sd.get_point(100, 400)
pentagon(point=point_pentagon, length=100, color=sd.random_color())

point_hexagon = sd.get_point(400, 400)
hexagon(point=point_hexagon, length=100, color=sd.random_color())

sd.pause()

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!
