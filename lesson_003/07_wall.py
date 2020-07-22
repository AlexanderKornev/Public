# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
from simple_draw import Point

sd.resolution = (1200, 600)
color = sd.COLOR_RED

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


for range_number, y in enumerate(range(0, 600, 50)):
    # TODO, Александр, лучше перенести условный оператор if/else в эту часть кода,
    #  создать дополнительную переменную, с которой будем начинать range для "x"
    #  Если чётный, то 0, если нет, то -50, как вы вычисляете в if/else. И в "for x in range(0, 1200, 100)" вместо 0,
    #  лучше передать нашу новую переменную. В таком случае:
    #  1. вычислений будет на порядок меньше.
    #  Сейчас "число вычислений" = "Число итераций цикла 1" * "Число итераций цикла 2".
    #  2. Не придётся изменять "x". Не изменяемые переменные в цикле лучше не переназначать - лишние действия.
    for x in range(0, 1200, 100):  # Идёт от -50 до 1200 не включительно с шагом 100
        if range_number % 2 == 0:
            y = y
            x = x
        else:
            y = y
            x = x - 50
        left_bottom = sd.get_point(x, y)
        right_top = sd.get_point(x + 100, y + 50)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_RED, width=1)


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
