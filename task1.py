# Создание класса "Моя строка" - доступны возможности str хранятся имя автора строки и время создания

import time


class MyStr(str):
    """Add class for str."""

    def __new__(cls, value, author):
        """Init new Str."""

        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.time()
        return instance

    def __str__(self):
        """Str for user"""

        return f"Для пользователя! Автор: {self.author}. Время: {self.time}"

    def __repr__(self):
        """Str for programmer"""

        return f"Для программиста! Автор: {self.author}. Время: {self.time}"


a = MyStr('Test Stroke', author='Author 1')

print(a.upper(), a.time, a.author)
print()
print(repr(a))
print(a)
