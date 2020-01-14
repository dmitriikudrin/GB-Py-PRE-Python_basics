"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
"""


class MyZeroDivisionError(Exception):
    """Класс-исключение, обрабатывающий ситуацию деления на нуль"""
    def __init__(self, number):
        """Метод конструктор, который возбуждает ошибку, если число равно 0"""
        if number == 0:
            raise self

    def __str__(self):
        """Переопределение метода отображения класса"""
        return "MyZeroDivisionError - К сожалению, на ноль делить нельзя:("


# Возбуждение и обработка ошибок
try:
    user_dividend = int(input("Введите делимое - "))
    user_divider = int(input("Введите делитель - "))
    MyZeroDivisionError(user_divider)
    print(f"Результат - {user_dividend / user_divider}")
except MyZeroDivisionError as e:
    print("Произошла ошибка:")
    print(e)
except ValueError as e:
    print("Произошла ошибка:")
    print(e)
