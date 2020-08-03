# -*- coding: utf-8 -*-
import simple_draw as sd
from epoch_making_canvas.smile import smile
sd.resolution = 1800, 800
# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)


from epoch_making_canvas import hoome_with_roof
from epoch_making_canvas.rainbow import rainbow
from epoch_making_canvas.sun import sun
from epoch_making_canvas import snowflake
from epoch_making_canvas.tree import draw_branches
from epoch_making_canvas.ground import ground

# TODO, Александр, предлагаю все используемые параметры для отрисовки указать в функциях, как паарметры по умолчанию.
#  В этом коде должны остаться только их вызовы. Анимируем картинку? =)
ground(45)
hoome_with_roof.home()
rainbow(500, 2000)
sun(800, 550, sd.COLOR_YELLOW)
root_point = sd.get_point(1000, 10)
draw_branches(point=root_point, angel=90, length=50)
root_point = sd.get_point(1100, 15)
draw_branches(point=root_point, angel=90, length=40, color=sd.COLOR_CYAN)
snowflake.snowfall(2)






# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
sd.pause()