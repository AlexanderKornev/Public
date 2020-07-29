# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1600, 800)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,


# def draw_branches(point, angel, length):
#     v1 = sd.get_vector(start_point=point, angle=angel, length=length, width=3)
#     v1.draw()
#     next_point = v1.end_point
#
#     v2 = sd.get_vector(start_point=next_point, angle=angel + 30, length=length * .75, width=3)
#     v2.draw()
#
#     v2 = sd.get_vector(start_point=next_point, angle=angel - 30, length=length * .75, width=3)
#     v2.draw()


# point_branches = sd.get_point(300, 0)
# draw_branches(point=point_branches, angel=90, length=50)
# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длина ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения
#  Александра, смотрите, задача такая. Рисуем 1 вектор снизу-вверх. Больше функция ничего не рисует.
#  Из его окончания берём начало для отрисовки двух других векторов.
#  Меняем длину и углы наклона векторов. - ГОТОВО
#  Вызываем функцию дважды с новыми параметрами - ГОТОВО

# def draw_branches(point, angel, length):
#     if length < 10:  #  условие выхода из фрактала лучше указывать в самую первую очередь.
#         return
#     v1 = sd.get_vector(start_point=point, angle=angel, length=length, width=1)
#     v1.draw()
#     angel_next_left = angel + 30
#     length_left = v1.length * 0.75
#     draw_branches(point=v1.end_point, angel=angel_next_left, length=length_left)
#     length_right = v1.length * 0.75
#     angel_next_right = angel - 30
#     draw_branches(point=v1.end_point, angel=angel_next_right, length=length_right)
#
#
# root_point = sd.get_point(300, 30)
# draw_branches(point=root_point, angel=90, length=100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

def draw_branches(point, angel, length):
    if length < 5:
        return
    v1 = sd.get_vector(start_point=point, angle=angel, length=length, width=1)
    v1.draw()
    angel_next_left = angel + sd.random_number(a=12, b=42)
    length_left = v1.length * (sd.random_number(a=60, b=90) / 100)
    draw_branches(point=v1.end_point, angel=angel_next_left, length=length_left)
    angel_next_right = angel - sd.random_number(a=12, b=42)
    length_right = v1.length * (sd.random_number(a=60, b=90) / 100)
    draw_branches(point=v1.end_point, angel=angel_next_right, length=length_right)


root_point = sd.get_point(300, 30)
draw_branches(point=root_point, angel=90, length=150)

# Пригодятся функции
# sd.random_number()

sd.pause()

# зачёт!
