# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
# и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
                       self.real * other.imaginary + self.imaginary * other.real)

    def __str__(self):
        return f"{self.real} + {self.imaginary}j"


my_complex_number_1 = Complex(2, 1)
my_complex_number_2 = Complex(-8, 7)
print(f"Сумма: {my_complex_number_1 + my_complex_number_2}")
print(f"Произведение: {my_complex_number_1 * my_complex_number_2}")

my_number_1 = complex(8, 4)
my_number_2 = complex(-7, 3)
print(my_number_1 + my_number_2)
print(my_number_1 * my_number_2)