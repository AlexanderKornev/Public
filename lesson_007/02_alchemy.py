# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __init__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())




class Water():
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Wind):
            return Storm()
        if isinstance(other, Fire):
            return Steam()
        if isinstance(other, Ground):
            return Mud()

class Wind():
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        if isinstance(other, Ground):
            return Dust()

class Fire():
    def __str__(self):
        return 'Огонь'
    def __add__(self, other):
        if isinstance(other, Ground):
            return Lava()

class Ground():
    def __str__(self):
        return 'Земля'

class Storm():
    def __str__(self):
        return 'ШТОООООРРРМ'

class Steam():
    def __str__(self):
        return 'Gabe Newell'

class Mud():
    def __str__(self):
        return 'Грязь!!!'

class Lightning():
    def __str__(self):
        return 'Молния!!!'

class Dust():
    def __str__(self):
        return 'пыль...'

class Lava():
    def __str__(self):
        return 'ЛАВА!!!!'
    

#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава
print(Water(), '+', Wind(), '=', Water() + Wind())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Ground(), '=', Water() + Ground())
print(Wind(), '+', Fire(), '=', Wind() + Fire())
print(Wind(), '+', Ground(), '=', Wind() + Ground())
print(Fire(), '+', Ground(), '=', Fire() + Ground())



class Could:
    def __str__(self):
        return 'ХОООЛОД'

    def __add__(self, other):
        if isinstance(other, Water):
            return Ice()
        if isinstance(other, Wind):
            return
        if isinstance(other, Fire):
            return
        if isinstance(other, Water):
            return



class Ice:
    def __str__(self):
        return 'Ice, ice, baby'


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
