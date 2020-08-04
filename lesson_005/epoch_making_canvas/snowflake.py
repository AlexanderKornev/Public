# -*- coding: utf-8 -*-
import simple_draw as sd

N = 20
def snowfall(n=5):
    quantity_snowflakes = n
    snowflake_dict = {}
    for number_x in range(quantity_snowflakes):
        x = sd.random_number(50, 100)
        y = sd.random_number(800, 850)
        length = sd.random_number(5, 15)
        snowflake_dict[number_x] = [x, y, length]

    while True:
        sd.start_drawing()
        for sf_name, value in snowflake_dict.items():
            x = value[0]
            y = value[1]
            length = value[2]
            point = sd.get_point(x, y)
            sd.snowflake(center=point, length=length, color=sd.background_color)
            value[0] += sd.random_number(-5, 5)
            value[1] -= sd.random_number(5, 20)
            point2 = sd.get_point(value[0], value[1])
            sd.snowflake(center=point2, length=length)
            if value[1] < 60:
                value[0] = sd.random_number(50, 100)
                value[1] = value[1] + 800
        sd.finish_drawing()
        sd.sleep(0.1)





