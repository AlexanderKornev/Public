# -*- coding: utf-8 -*-
import simple_draw as sd

def rainbow(point_x, end_point_x):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    for _ in rainbow_colors :
        point = sd.get_point(point_x, 1500)
        end_point = sd.get_point(end_point_x, 300)
        sd.line(start_point=point, end_point=end_point, color=_, width=9)
        point_x += 10
        end_point_x += 10



