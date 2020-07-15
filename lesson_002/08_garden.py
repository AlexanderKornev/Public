#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза',)

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка',)

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов
all_flowers = garden_set | meadow_set
print('Все виды цветов:', all_flowers)

# выведите на консоль те, которые растут и там и там
flowers_matshes = garden_set & meadow_set
print('Растут и в саду и на лугу:', flowers_matshes)

# выведите на консоль те, которые растут в саду, но не растут на лугу
garden_more_meadow = garden_set - meadow_set
print('Растут в саду, но не растут на лугу:', garden_more_meadow)

# выведите на консоль те, которые растут на лугу, но не растут в саду
meadow_more_garden = meadow_set - garden_set
print('Растут на лугу, но не растут в саду:', meadow_more_garden)

# зачёт!
