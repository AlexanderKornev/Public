#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Tanya', 'Andrey', 'Lena', 'Ira'
]


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [my_family[0], 165], [my_family[1], 170], [my_family[2], 168], [my_family[3], 160]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца - ', my_family_height[1][1], 'см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
total_family_height = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1]
print('Общий рост моей семьи - ', total_family_height, 'см')