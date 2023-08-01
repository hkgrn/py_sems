# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.


import random

class NumberGuesser:
    def __init__(self):
        self.number = random.randint(0, 1000)
        self.attempts = 0
        self.finished = False

    def guess(self, num):
        if num < 0 or num > 1000:
            return "Число должно быть в диапазоне от 0 до 1000. Попробуй еще раз."

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
    num = int(input("Угадай число от 0 до 1000: "))
    result = guesser.guess(num)
    print(result)