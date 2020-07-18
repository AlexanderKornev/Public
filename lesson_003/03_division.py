# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя ни одной из операций деления: ни деления с плавающей точкой /, ни целочисленного деления //
# и взятия остатка %
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37
integer = 0
multiplication_a = a
multiplication_b = b

while multiplication_a >= multiplication_b:
    integer += 1
    multiplication_a -= multiplication_b


print('Целочисленное деление', a, 'на', b, 'дает', integer)
