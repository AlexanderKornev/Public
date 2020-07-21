# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
from simple_draw import Point

sd.resolution = (1200, 600)
color = sd.COLOR_RED

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

x = 0
y = 0
for range_number, y in enumerate(range(0, 600, 50)):
    if range_number % 2 == 0:
        y = y
    else:
        y1 = y + 50

    # TODO, Александр, давайте попробуем упростить. Вложенный оператор if/else в цикле ниже не нужен.
    #  изменение y1 и y.
    #  Давайте попробуем с помощью определения чётности ряда, определаить начало рисования первого кирпича.
    #  Первую координату "x". Если ряд чётный, то начинаем с "0", если ряд не чётный,
    #  то с середины длины кирпича (-50 к примеру). Создадим переменную, в которой будет или 0 или -50 и передадим
    #  её в range ниже. как точка с которой начинаем рисовать. Сейчас это -50.
    for x in range(-50, 1200, 100):  # Идёт от -50 до 1200 не включительно с шагом 100
        x = x
        if range_number % 2 == 0:
            left_bottom = sd.get_point(x, y)
            right_top = sd.get_point(x + 100, y + 50)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_RED, width=1)
        else:
            x += 50
            left_bottom1 = sd.get_point(x, y)
            right_top2 = sd.get_point(x + 100, y1)
            sd.rectangle(left_bottom=left_bottom1, right_top=right_top2, color=sd.COLOR_RED, width=1)

        # left_bottom1 = sd.get_point(x2, y)
        # right_top2 = sd.get_point(x2 + 100, y + 50)
        # sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_RED, width=1)

# Я не понимаю, как нужно сделать сдвиг.
# В чате пишут, что нужно добавить if, которое проверяло бы шаг на четность и в зависимости
# от этого скрипт рисовал бы квадрат со сдвигом. Но я не понимаю, как пропустить обычный шаг.
# Я примерно понимаю, как сдвиг работает, но как его зациклить...

# x = 0
# y = 0
# x1 = 100
# y1 = 50
# left_bottom = sd.get_point(x, y)
# right_top = sd.get_point(x1, y1)
# sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_CYAN, width=1)
#
# x = 50
# y = 50
# x1 = 150
# y1 = 100
# left_bottom = sd.get_point(x, y)
# right_top = sd.get_point(x1, y1)
# sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_CYAN, width=1)




# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

sd.pause()
