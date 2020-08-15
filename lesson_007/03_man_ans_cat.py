# -*- coding: utf-8 -*-


from random import randint
from termcolor import cprint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 100
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness,
        )

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def buy_cat_food(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой котику'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50

    def clean_house(self):
        if self.house.dirt >= 100:
            cprint('{} убрался в доме!'.format(self.name), color='magenta')
        self.fullness -= 20
        self.house.dirt -= 100


    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif self.house.food < 20:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.cat_food < 10:
            self.buy_cat_food()
        elif self.house.dirt >= 100:
            self.clean_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()

    def get_cat(self, name_cat, house):
        Cat(name_cat).house = house  # не понимаю, как внутри этого метода присвоить значение атрибуту внутри
        # TODO в этом месте Вы вызываете класс Кота. Вот пример Вашего кода, где вызываете и сохраняете класс Кота
        #  felix = Cat(name='Феликс')
        #  Дальше подбираете кота
        #  bivis.get_cat(name_cat=felix, house=my_sweet_home)
        #  Получается Cat(name_cat).house = house равно Cat(Cat(name='Феликс')).house = house
        #  name_cat это не имя кота, а Класс кота.
        #  У класса Кот, есть аргумент house. Давайте попробуем поселить кота так же, как селим человека.

        # в свой дом
        # инита кота. Сейчас прописано жестко
        self.fullness -= 10
        cprint('Взяли кота {} в дом'.format(name_cat), color='cyan')

class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 0
        self.dirt = 0
        

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, кошачьей еды осталось {}, грязно на {}'.format(
            self.food, self.money, self.cat_food, self.dirt
        )

class Cat:

    house = None

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = my_sweet_home  # В этом месте должен быть просто None. Коту мы дом потом присвоим =)

    def __str__(self):
        return '{} - зе кот! Сытость {}'.format(self.name, self.fullness)

    def eat(self):
        # TODO, Александр, давайте немного поменяем условие. Если кошачьей еды больше или равно тому,
        #  что может съесть кот определённого кол-ва, то кот есть. В противном случае - скончается.
        if self.house.cat_food <= 0:
            cprint('Котик {} скончался от недостатка в питании..'.format(self.name), color='red')
            return
        cprint('Котик {} вкусно кушает и облизывается.'.format(self.name))
        self.fullness += 20
        self.house.cat_food -= 10

    def sleep(self):
        if self.fullness <= 0:
            cprint('Котик {} скончался от недостатка в питании..'.format(self.name), color='red')
            return
        self.fullness -= 10
        cprint('Котик {} сладко спит.'.format(self.name), color='grey')

    def play(self):
        if self.fullness <= 0:
            cprint('Котик {} скончался от недостатка в питании..'.format(self.name), color='red')
            return
        self.fullness -= 10
        self.house.dirt += 5
        cprint('Котик {} играет с обоями..'.format(self.name), color='grey')

    def do_nothing(self):
        if self.fullness <= 0:
            cprint('Котик {} скончался от недостатка в питании..'.format(self.name), color='red')
            return
        self.fullness -= 5
        cprint('Я котик по имени {} и сейчас я не делаю ничего!'.format(self.name), color='cyan')


    def cat_act(self):
        if self.fullness <= 0:
            cprint('Котик {} скончался от недостатка в питании..'.format(self.name), color='red')
            return
        decision = randint(1, 3)
        if self.fullness < 20:
            self.eat()
        if decision == 1:
            self.sleep()
        elif decision == 2:
            self.play()
        else:
            self.do_nothing()


# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

bivis = Man(name='Бивис')
my_sweet_home = House()
bivis.go_to_the_house(house=my_sweet_home)

# TODO, предлагаю подумать, как добавлять котов в цикле
felix = Cat(name='Феликс')
bivis.get_cat(name_cat=felix, house=my_sweet_home)
edmund = Cat(name='Эдмунд')
bivis.get_cat(name_cat=edmund, house=my_sweet_home)
bigglesworth = Cat(name='Бигглсуорт')
bivis.get_cat(name_cat=bigglesworth, house=my_sweet_home)
# leopold = Cat(name='Леопольд')
# bivis.get_cat(name_cat=leopold, house=my_sweet_home)
# TODO, Александр, пожалуйста, обратите внимание, все в итоге должны выжить =)
for day in range(1, 365):
    print('================ день {} =================='.format(day))
    bivis.act()
    felix.cat_act()
    edmund.cat_act()
    bigglesworth.cat_act()
    # leopold.cat_act()
    print('--- в конце дня ---')
    print(bivis)
    print(felix, ',',
          edmund, ',',
          bigglesworth, ',',)
          # leopold)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
