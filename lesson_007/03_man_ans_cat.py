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
        if self.house.food >= 20:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.food -= 20
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
        if self.house.dirt >= 50:
            cprint('{} убрался в доме!'.format(self.name), color='magenta')
        self.fullness -= 20
        self.house.dirt -= 100


    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        self.buy_cat_food()
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.money < 50:
            self.work()
        elif self.house.food <= 20:
            self.shopping()
        elif self.house.cat_food <= 50:
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
        Cat.house = house
        self.fullness -= 10
        cprint('Взяли кота {} в дом'.format(name_cat), color='cyan')

class House:

    def __init__(self):
        self.food = 50
        self.money = 50
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
        # self.house = my_sweet_home  # В этом месте должен быть просто None. Коту мы дом потом присвоим =)

    def __str__(self):
        return '{} - зе кот! Сытость {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('Котик {} вкусно кушает и облизывается.'.format(self.name))
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint('Котик {} скончался от недостатка в питании..'.format(self.name), color='red')
            return

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

    def cat_act(self):
        if self.fullness <= 0:
            cprint('Котик {} скончался от недостатка в питании..'.format(self.name), color='red')
            return
        if self.fullness < 30:
            self.eat()
        decision = randint(1, 2)
        if decision == 1:
            self.sleep()
        elif decision == 2:
            self.play()


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

cats = [ Cat(name='Феликс'),
        Cat(name='Эдмунд'),
    Cat(name='Бигглсуорт')
]

for cat in cats:
    bivis.get_cat(name_cat=cat, house=my_sweet_home)

for day in range(1, 365):
    print('================ день {} =================='.format(day))
    bivis.act()
    for cat in cats:
        cat.cat_act()
    print('--- в конце дня ---')
    for cat in cats:
        print(cat)
    print(bivis)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
