# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (600, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

point_x = 50
end_point_x = 350


for _ in rainbow_colors:
    point = sd.get_point(point_x, 50)
    end_point = sd.get_point(end_point_x, 450)
    sd.line(start_point=point, end_point=end_point, color=_, width=4)
    point_x += 5
    end_point_x += 5


# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
point = sd.get_point(-20, -100)
radius = 500
for _ in rainbow_colors[::-1]:
    radius += 16
    sd.circle(center_position=point, radius=radius, color=_, width=15)

sd.pause()
