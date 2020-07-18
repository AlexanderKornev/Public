a = int(input('Введите любое число: '))
b = int(input('Введите число меньше первого: '))
integer = 0
multiplication_a = a
multiplication_b = b

while multiplication_a >= multiplication_b:
    integer += 1
    multiplication_a -= multiplication_b


print('Целочисленное деление', a, 'на', b, 'дает', integer)