# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 1000)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()




quantity_snowflakes = 100
snowflake_dict = {}
for number_x in range(quantity_snowflakes) :
    x = sd.random_number(100, 1100)
    y = sd.random_number(700, 800)
    length = sd.random_number(5, 12)
    snowflake_dict[number_x] = [x, y, length]
    print(snowflake_dict)
    #first_position.setdefault('snowflake' + str(number_x), [x, y, length])


while True:
        sd.start_drawing()
        # TODO, Классно получилось. Только, по словарю лучше идти в цикле с помощью items().
        #  Переделайте пожалуйста и уберите лишний print  будет зачёт =)
        for index, sf_name in enumerate(snowflake_dict):
            x = snowflake_dict[sf_name][0]
            y = snowflake_dict[sf_name][1]
            length = snowflake_dict[sf_name][2]
            point = sd.get_point(x, y)
            sd.snowflake(center=point, length=length, color=sd.background_color)
            snowflake_dict[sf_name][0] = snowflake_dict[sf_name][0] + sd.random_number(-5, 5)
            snowflake_dict[sf_name][1] = snowflake_dict[sf_name][1] - sd.random_number(5, 20)
            point2 = sd.get_point(snowflake_dict[sf_name][0], snowflake_dict[sf_name][1])
            sd.snowflake(center=point2, length=length)
            if snowflake_dict[sf_name][1] < 12:
                snowflake_dict[sf_name][0] = sd.random_number(100, 1100)
                snowflake_dict[sf_name][1] = snowflake_dict[sf_name][1] + 800
        sd.finish_drawing()
        sd.sleep(0.1)

        # for index, sf_name in enumerate(secound_dic):
        #     x = secound_dic[sf_name][0]
        #     y = secound_dic[sf_name][1]
        #     length = secound_dic[sf_name][2]
        #     point = sd.get_point(x, y)
        #     sd.snowflake(center=point, length=length, color=sd.background_color)
        # sd.sleep(0.1)
        # # sd.finish_drawing()
        if sd.user_want_exit():
            print(snowflake_dict)
            break



sd.pause()



# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       изменить координата_у и запомнить её в списке по индексу
#       создать точку отрисовки снежинки по координатам
#       нарисовать снежинку белым цветом в этой точке
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла: полная очистка всего экрана - долгая операция.
# - использовать хак для стирания старого положения снежинки:
#       отрисуем её заново на старом месте, но цветом фона (sd.background_color) и она исчезнет!
# - использовать функции sd.start_drawing() и sd.finish_drawing()
#       для начала/окончания отрисовки кадра анимации
# - между start_drawing и finish_drawing библиотека sd ничего не выводит на экран,
#       а сохраняет нарисованное в промежуточном буфере, за счет чего достигается ускорение анимации
# - в момент вызова finish_drawing все нарисованное в буфере разом покажется на экране
#
# Примерный алгоритм ускоренной отрисовки снежинок
#   навсегда
#     начать рисование кадра
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     закончить рисование кадра
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

