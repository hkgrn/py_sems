# Класс прямоугольник. Возможность сложения и вычитания. Должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длину и ширину. При вычитании не должно быть отрицательных значений.

class Rectangle:
    """Add Class Rectangle."""

    def __init__(self, width, lenght):
        """Init new Ex."""
        self.width = width
        self.lenght = lenght

    def area(self):
        """Area of Rectangle."""
        return self.width * self.lenght

    def perimetr(self):
        """Perimetr of Rectangle."""

        return 2 * (self.width + self.lenght)

    def __add__(self, other):
        """Summ of two rectangles."""

        summ_perim = self.perimetr() + other.perimetr()
        width_rectangle_c = self.width
        lenght_rectangle_c = summ_perim / 2 - width_rectangle_c
        return Rectangle(width_rectangle_c, lenght_rectangle_c)

    def __sub__(self, other):
        """Sub of two rectangles."""

        sub_perim = abs(self.perimetr() - other.perimetr())
        width_rectangle_c = min(self.width, other.width, self.lenght, other.lenght)
        lenght_rectangle_c = sub_perim / 2 - width_rectangle_c
        return Rectangle(width_rectangle_c, lenght_rectangle_c)

    def __eq__(self, other):  # равенство
        """EQ of two rectangles."""

        return self.area() == other.area()

    def __ne__(self, other):  # неравенство
        """NE of two rectangles."""

        return self.area() != other.area()

    def __lt__(self, other):  # меньше <
        """LT of two rectangles."""

        return self.area() < other.area()

    def __le__(self, other):  # меньше или равно <=
        """LE of two rectangles."""

        return self.area() <= other.area()

    def __gt__(self, other):  # больше >
        """GT of two rectangles."""

        return self.area() > other.area()

    def __ge__(self, other):  # больше или равно >=
        """GE of two rectangles."""

        return self.area() >= other.area()

    def __str__(self):
        """Str for user"""

        return f"Для пользователя! Площадь прямоугольника: {self.area()}. Периметр: {self.perimetr()} "

    def __repr__(self):
        """Str for programmer"""

        return f"Для программиста! Площадь: {self.area()}. Периметр: {self.perimetr()}"


rectangle_a = Rectangle(2, 3)
rectangle_b = Rectangle(5, 10)

print("[1] ", rectangle_a, " | ", repr(rectangle_a))
print("[2] ", rectangle_b, " | ", repr(rectangle_b))

rectangle_c = rectangle_a + rectangle_b
print("[СЛОЖЕНИЕ] ", rectangle_c, " | ", repr(rectangle_c))

rectangle_d = rectangle_a - rectangle_b
print("[ВЫЧИТАНИЕ] ", rectangle_d, " | ", repr(rectangle_d))

print("[СРАВНЕНИЕ] ", rectangle_a != rectangle_b)