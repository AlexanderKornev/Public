# -*- coding: utf-8 -*-
import simple_draw as sd



def draw_branches(point=sd.get_point(1000, 10), angel=90, length=50, color=sd.COLOR_YELLOW):
    if length < 5:
        return
    v1 = sd.get_vector(start_point=point, angle=angel, length=length, width=1)
    v1.draw(color=color)
    angel_next_left = angel + sd.random_number(a=12, b=42)
    length_left = v1.length * (sd.random_number(a=60, b=90) / 100)
    draw_branches(point=v1.end_point, angel=angel_next_left, length=length_left, color=color)
    angel_next_right = angel - sd.random_number(a=12, b=42)
    length_right = v1.length * (sd.random_number(a=60, b=90) / 100)
    draw_branches(point=v1.end_point, angel=angel_next_right, length=length_right, color=color)


def draw_branches1(point=sd.get_point(1100, 15), angel=90, length=40, color=sd.COLOR_CYAN):
    if length < 5:
        return
    v1 = sd.get_vector(start_point=point, angle=angel, length=length, width=1)
    v1.draw(color=color)
    angel_next_left = angel + sd.random_number(a=12, b=42)
    length_left = v1.length * (sd.random_number(a=60, b=90) / 100)
    draw_branches(point=v1.end_point, angel=angel_next_left, length=length_left, color=color)
    angel_next_right = angel - sd.random_number(a=12, b=42)
    length_right = v1.length * (sd.random_number(a=60, b=90) / 100)
    draw_branches(point=v1.end_point, angel=angel_next_right, length=length_right, color=color)
# Пригодятся функции
# sd.random_number()
