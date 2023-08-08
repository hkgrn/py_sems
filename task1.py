"""Создайте класс студента.
Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых."""

import csv


class NameValidation:
    """Проверка ФИО"""

    def __set_name__(self, owner, name):
        """Защита имени"""

        self.name = "_" + name

    def __get__(self, instance, owner):
        """Возвращаем значение"""

        return getattr(instance, self.name)

    def valid(self, value):
        """Проверка на str и alpha"""

        if value != value.capitalize() or not value.isalpha():
            raise TypeError('Error: Type or not alpha')


    def __set__(self, instance, value):
        """Присваиваем значение"""

        self.valid(value)
        setattr(instance, self.name, value)


class Student:
    firstname = NameValidation()
    lastname = NameValidation()

    def __init__(self, firstname, lastname):
        """Инициализация"""

        self.firstname = firstname
        self.lastname = lastname

    def av_rating(self):
        """Средняя оценка"""

        averages = {}
        with open('Subjects.csv', 'r', encoding='utf-8', newline='') as r_file:
            filereader = csv.DictReader(r_file, delimiter=';')
            for line in filereader:
                grades = list(map(int, line['Grades'].split()))
                tests = list(map(int, line['Tests'].split()))

                grades_rate = sum(grades) / len(grades)
                tests_rate = sum(tests) / len(tests)

                averages[line['Lesson']] = (grades_rate, tests_rate)

        print(f"РЕЗУЛЬТАТЫ СТУДЕНТА [{self.firstname} {self.lastname}]:\n")

        for k, j in averages.items():
            print(f'Предмет: {k} \nСредняя оценка: {j[0]} | Средний балл тестов: {j[1]}\n')

        sum_grades = sum([float(k[0]) for _, k in averages.items()])
        sum_test = sum([float(k[1]) for _, k in averages.items()])

        print("Общая средняя оценка:", (sum_grades / len(averages)),"|", "Общий средний балл (тесты):", (sum_test / len(averages)))

test = Student('Михаил', 'Иванов')
test.av_rating()