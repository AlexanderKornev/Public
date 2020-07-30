# -*- coding: utf-8 -*-
import random

while True:
    user_input = input('Введите: камень, ножницы или бумагу: ')
    list = ['камень', 'ножницы', 'бумага']
    x = random.randint(0, 2)
    print(x)
    pc_victory = ('Результат - PC выиграл!', ' Вы выкинули:', user_input, 'Компьютер выкинул:', list[x])
    human_victory = ('Результат - Вы выиграли!', ' Вы выкинули:', user_input, 'Компьютер выкинул:', list[x])
    if user_input == list[x]:
        print('Результат - ничя!', 'Вы выкинули:', user_input, 'Компьютер выкинул:', list[x])
    if list[x] == 'камень' and user_input == 'ножницы':
        print(pc_victory)
    if list[x] == 'камень' and user_input == 'бумага':
        print(human_victory)
    if list[x] == 'ножницы' and user_input == 'камень':
        print(human_victory)
    if list[x] == 'ножницы' and user_input == 'бумага':
        print(pc_victory)
    if list[x] == 'бумага' and user_input == 'камень':
        print(pc_victory)
    if list[x] == 'бумага' and user_input == 'ножницы':
        print(human_victory)

# print(random.randint(0, 100))