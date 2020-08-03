# -*- coding: utf-8 -*-
import simple_draw as sd
from epoch_making_canvas.smile import smile


def home():
    def wall():
        for range_number, y in enumerate(range(50, 250, 50)):
            range_x = 430 if range_number % 2 == 0 else 380
            for x in range(range_x, 860, 100):  # Идёт от -50 до 1200 не включительно с шагом 100
                left_bottom = sd.get_point(x, y)
                right_top = sd.get_point(x + 100, y + 50)
                sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_RED, width=1)

    wall()
    # убираем лишние кирпичи слева
    # Интересное решение, как вариант, можно было поменьше нарисовать
    # стену в этом range(range_x, 860, 100) и этом range(50, 250, 50) местах =)
    left_bottom = sd.get_point(370, 50)
    right_top = sd.get_point(429, 250)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.background_color, width=0)
    # убираем лишние кирпичи справа
    left_bottom = sd.get_point(860, 50)
    right_top = sd.get_point(950, 250)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.background_color, width=0)
    # фон для окна
    left_bottom = sd.get_point(550, 100)
    right_top = sd.get_point(700, 180)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.background_color, width=0)
    # окно
    left_bottom = sd.get_point(550, 100)
    right_top = sd.get_point(700, 180)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_YELLOW, width=3)
    window_point = sd.get_point(600, 100)
    window_point1 = sd.get_point(600, 180)
    sd.line(start_point=window_point, end_point=window_point1, width=3)
    window_point2 = sd.get_point(550, 150)
    window_point3 = sd.get_point(600, 150)
    sd.line(start_point=window_point2, end_point=window_point3, width=3)
    # смайл в окне
    smile(x=650, y=140, color=sd.COLOR_YELLOW)
    # каркас дома
    left_bottom = sd.get_point(430, 50)
    right_top = sd.get_point(860, 250)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_DARK_RED, width=4)
    # крыша дома
    point1 = sd.get_point(390, 250)
    point2 = sd.get_point(900, 250)
    point3 = sd.get_point(645, 350)

    point_list = [point1, point2, point3]

    sd.polygon(point_list=point_list, width=0)
    return

# if __name__ == '__main__':
#     home()
