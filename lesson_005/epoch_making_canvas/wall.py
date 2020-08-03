# -*- coding: utf-8 -*-
import simple_draw as sd
from simple_draw import Point

sd.resolution = (1200, 600)
color = sd.COLOR_RED

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

def wall():
    for range_number, y in enumerate(range(0, 600, 50)):

        range_x = 0 if range_number % 2 == 0 else -50

        for x in range(range_x, 1200, 100):  # Идёт от -50 до 1200 не включительно с шагом 100
            left_bottom = sd.get_point(x, y)
            right_top = sd.get_point(x + 100, y + 50)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_RED, width=1)




sd.pause()