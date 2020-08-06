# -*- coding: utf-8 -*-
import simple_draw as sd
sd.resolution = 1800, 800
from random import randint
def rainbow(point_x=500, end_point_x=2000):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    ran = randint(0, 1)
    if ran == 0:
        for _ in rainbow_colors :
            point = sd.get_point(point_x, 1500)
            end_point = sd.get_point(end_point_x, 300)
            sd.line(start_point=point, end_point=end_point, color=_, width=9)
            sd.sleep(0.1)
            point_x += 10
            end_point_x += 10
    else:
        for _ in rainbow_colors :
            point = sd.get_point(point_x, 1500)
            end_point = sd.get_point(end_point_x, 300)
            sd.line(start_point=point, end_point=end_point, color=sd.invert_color(_), width=9)
            sd.sleep(0.1)
            point_x += 10
            end_point_x += 10





