import simple_draw as sd

def ground(high):
    point1 = sd.get_point(-1, -1)
    point2 = sd.get_point(2000, -1)
    point3 = sd.get_point(2000, high)
    point4 = sd.get_point(-1, high)

    point_list = [point1, point2, point3, point4]

    sd.polygon(point_list=point_list, width=0, color=sd.COLOR_DARK_GREEN)

