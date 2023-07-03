# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

CONVERT = 16

num = int(input('Введите целое число: '))
div = None
result = ''

print(f'Проверка с помощью hex: {hex(num)}')

while num >= 1:
    div = num % CONVERT
    if div < 10:
        result += str(div)
    else:
        if div == 10:
            result += str('a')
        if div == 11:
            result += str('b')
        if div == 12:
            result += str('c')
        if div == 13:
            result += str('d')
        if div == 14:
            result += str('e')
        if div == 15:
            result += str('f')
    num //= CONVERT

print(f'Результат вычислений: 0x{result[::-1]}')

