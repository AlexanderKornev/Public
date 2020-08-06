# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

import lesson_005.my_burger as mb

mb.add_buns()
mb.add_cutlet()
mb.add_cheese()
mb.add_cutlet()
mb.add_cheese()
mb.add_cucumber()
mb.add_tomato()
mb.add_mayo()
mb.add_buns()

print('БигМак:')
mb.add_buns()
mb.add_salat()
mb.add_cheese()
mb.add_cutlet()
mb.add_sauce()
mb.add_buns()
mb.add_sauce()
mb.add_salat()
mb.add_cucumber()
mb.add_cutlet()
mb.add_bunss()

# зачёт!
