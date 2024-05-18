# Требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник. Для этого создайте класс TriangleChecker, принимающий только положительные числа. С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
# Ура, можно построить треугольник!
# С отрицательными числами ничего не выйдет!
# Жаль, но из этого треугольник не сделать.

class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if self.a < 0 or self.b < 0 or self.c < 0:
            return "С отрицательными числами ничего не выйдет!"
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return "Жаль, но из этого треугольник не сделать."
        return "Ура, можно построить треугольник!"


a = int(input("Введите длину стороны a: "))
b = int(input("Введите длину стороны b: "))
c = int(input("Введите длину стороны c: "))


triangle_checker = TriangleChecker(a, b, c)
result = triangle_checker.is_triangle()

print(result)

