# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
need_in_month = 0
total_expenses = 0
inflation = 0


# while months > month_number:
#     total_expenses += need_in_month
#     month_number += 1
#     if month_number == 2:
#         total_expenses += inflation * need_in_month
#     if month_number > 2:
#         inflation += 0.03
#         total_expenses += inflation * need_in_month
#     continue
# print('Студенту надо попросить', total_expenses, 'рублей')


# Я не до конца понимаю условие задачи. Получается, что в первый месяц, студенту нужно будет дополнительно только 2000?
# Т.Е. в первый месяц инфляция не учитывается? Считать инфляция и увеличиваться
count = 0
while count < 9:
    count += 1
    need_in_month = expenses - educational_grant
    total_expenses += need_in_month
    inflation += 0.03
    expenses += inflation * expenses
    continue
print('Студенту надо попросить', total_expenses.__round__(2), 'рублей')