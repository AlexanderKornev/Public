# -*- coding: utf-8 -*-
import simple_draw as sd
def smile(x, y, color):
    # Рисуем круг смайла
    point = sd.get_point(x, y)
    sd.circle(center_position=point, radius=40, color=color, width=5)
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


