# Создайте функцию генератор чисел Фибоначчи

def fibo(num: int) -> list:
    first, second = 0, 1  # В ЧФ первые два числа равны 0 и 1
    for i in range(num):
        yield first # Передаем каждое значение с сохранением
        first, second = second, first + second


number = int(input('Введите количество чисел в последовательности: '))
print('Последовательность: ', *fibo(number))
