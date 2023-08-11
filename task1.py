# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.


import random


class UserException(Exception):
    pass


class RangeError(UserException):
    def __init__(self, num, min_el, max_el):
        self.num = num
        self.min = min_el
        self.max = max_el

    def __str__(self):
        return f'Число должно быть в диапазоне от {self.min} до {self.max}. Вы задали число: {self.num}. Попробуйте еще раз.'


class NotIntError(UserException):
    def __init__(self):
        pass

    def __str__(self):
        return f'Введенное значение должно быть числом int().'


class NumberGuesser:
    def __init__(self):
        self.number = random.randint(0, 1000)
        self.attempts = 0
        self.finished = False

    def guess(self, num):
        min_el = 0
        max_el = 1000
        if num < min_el or num > max_el:
            raise RangeError(num, min_el, max_el)

        self.attempts += 1
        if num == self.number:
            self.finished = True
            return f"Поздравляю! Ты угадал число {self.number} за {self.attempts} попыток. Молодец!"
        elif self.attempts >= 10:
            print(f"К сожалению, ты исчерпал все попытки. Число было {guesser.number}. Попробуй снова!")
            self.finished = True
        elif num < self.number:
            return "Больше! Попробуй еще раз."
        else:
            return "Меньше! Попробуй еще раз."


guesser = NumberGuesser()

while not guesser.finished:
    try:
        num = int(input("Угадай число от 0 до 1000: "))
    except:
        raise NotIntError()
    result = guesser.guess(num)
    print(result)
