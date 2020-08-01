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

mb.buns()
mb.cutlet()
mb.cheese()
mb.cutlet()
mb.cheese()
mb.cucumber()
mb.tomato()
mb.mayo()
mb.buns()


print('БигМак:')
mb.buns()
mb.salat()
mb.cheese()
mb.cutlet()
mb.sauce()
mb.buns()
mb.sauce()
mb.salat()
mb.cucumber()
mb.cutlet()
mb.bunss()
