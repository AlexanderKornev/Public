import simple_draw as sd
from random import randint
def sun(x=800, y=500, color=sd.COLOR_YELLOW):
    # Рисуем круг смайла
    point = sd.get_point(x, y)
    sd.circle(center_position=point, radius=40, color=color, width=0)
    ran = randint(0, 1)
    if ran == 0 :
        for angle in range(0, 360, 20):
            v1 = sd.get_vector(start_point=point, angle=angle, width=5, length=100)
            v1.draw(color=color)
    else:
        sd.circle(center_position=point, radius=40, color=sd.COLOR_DARK_YELLOW, width=0)
        for angle in range(0, 360, 20):
            v1 = sd.get_vector(start_point=point, angle=angle, width=5, length=100)
            v1.draw(color=sd.COLOR_DARK_YELLOW)
