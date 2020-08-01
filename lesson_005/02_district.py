# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

import lesson_005.district.central_street.house1.room1 as central_h1_r1
import lesson_005.district.central_street.house1.room2 as central_h1_r2
import lesson_005.district.central_street.house2.room1 as central_h2_r1
import lesson_005.district.central_street.house2.room2 as central_h2_r2

import lesson_005.district.soviet_street.house1.room1 as soviet_h1_r1
import lesson_005.district.soviet_street.house1.room2 as soviet_h1_r2
import lesson_005.district.soviet_street.house2.room1 as soviet_h2_r1
import lesson_005.district.soviet_street.house2.room2 as soviet_h2_r2

comma = ', '
print('На районе живут:'
      , comma.join(central_h1_r1.folks)
      , comma.join(central_h1_r2.folks)
      , comma.join(central_h2_r1.folks)
      , comma.join(central_h2_r2.folks)
      , comma.join(soviet_h1_r1.folks)
      , comma.join(soviet_h1_r2.folks)
      , comma.join(soviet_h2_r1.folks)
      , comma.join(soviet_h2_r2.folks))
