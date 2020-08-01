# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...
from os.path import join

import lesson_005.room_1 as r1
import lesson_005.room_2 as r2
comma = ', '
print('В комнате room_1 живут:', s.join(r1.folks))
print('В комнате room_2 живут:', s.join(r2.folks))

