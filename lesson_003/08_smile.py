# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(x, y, color):
    # Рисуем круг смайла
    point = sd.get_point(x, y)
    sd.circle(center_position=point, radius=50, color=color, width=5)
    # Рисуем левый глаз
    left_eye = sd.get_point(x - 15, y + 20)
    sd.circle(center_position=left_eye, radius=5, color=color, width=2)
    # Рисуем правый глаз
    right_eye = sd.get_point(x + 15, y + 20)
    sd.circle(center_position=right_eye, radius=5, color=color, width=2)
    # Рисуем нос
    nose_start = sd.get_point(x, y + 15)
    nose_end = sd.get_point(x, y)
    sd.line(nose_start, nose_end, color=color, width=3)
    # Рисуем центр рта
    mouth_1_start = sd.get_point(x - 15, y - 20)
    mouth_1_end = sd.get_point(x + 15, y - 20)
    sd.line(mouth_1_start, mouth_1_end, color=color, width=2)
    # Рисуем левую часть рта
    mouth_2_start = mouth_1_start
    mouth_2_end = sd.get_point(x - 15, y - 10)
    sd.line(mouth_2_start, mouth_2_end, color=color, width=2)
    # Рисуем правую часть рта
    mouth_3_start = mouth_1_end
    mouth_3_end = sd.get_point(x + 15, y - 10)
    sd.line(mouth_3_start, mouth_3_end, color=color, width=2)


# По условиям задачи, x и y должны быть константами. Я не понимаю, как их рандомизировать для
# скрипта. У них должно быть значение int(), поэтому функция sd.random_point() не работает.
# Прошу "натолкнуть" в нужное русло.

# Понял, что функция sd.random_point возвращается объект (класс) Point,
# который возвращает себя и две функции x и y.
# Когда мы вызвали функцию, мы можем обратиться к функции x и y,
# что бы они вернули нам случайные числа из диапазона точек видимого экрана.
# Я все правильно расписал, Владимир?
for _ in range(10):
    point = sd.random_point()
    point_x, point_y = point.x, point.y
    smile(x=point_x, y=point_y, color=sd.random_color())
# Я увеличил range до 1000, интересно получилось =)
sd.pause()

# зачёт!
