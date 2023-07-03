# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей. Для проверки своего кода используйте модуль fractions.

import fractions

# Ввод
first_inp: str = input('Введите первую дробь через "/": ')
second_inp: str = input('Введите вторую дробь через "/": ')

fraction_1 = first_inp.split('/')
fraction_2 = second_inp.split('/')

up_1 = int(fraction_1[0])
up_2 = int(fraction_2[0])

down_1 = int(fraction_1[1])
down_2 = int(fraction_2[1])

# Блок проверки
sum_fractions = fractions.Fraction(up_1, down_1) + fractions.Fraction(up_2, down_2)
prod_fractions = fractions.Fraction(up_1, down_1) * fractions.Fraction(up_2, down_2)
print('Проверка с помощью fractions. Сумма: ' + str(sum_fractions) + '. Произведение: ' + str(prod_fractions) + '.')

# Решение
summ = ''
summ_up = 0
summ_down = 0
start = 1
stop = 9

prod: str = str(up_1*up_2)+'/'+str(down_1*down_2)

summ_up = up_1*down_2 + up_2*down_1
summ_down = down_1*down_2
for i in range(start, stop):
    if summ_up % i == 0 and summ_down % i == 0:
        summ = str(summ_up//i)+'/'+str(summ_down//i)
    else:
        summ = str(summ_up)+'/'+str(summ_down)

print(f'Полученный результат. Сумма: {summ}. Произведение: {prod}.')