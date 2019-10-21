"""
Программа принимает действительное положительное число x и целое отрицательное
число y. Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения
числа в степень.
"""


def exponentiation():
    # Определение функции, возводящей число в отрицательную степень

    # Ввод начальных данных
    number = input("Введите число - ")
    power = input("Введите степень - ")

    # Проверка корректности ввода
    if number.isdigit() and power.lstrip('-').isdigit():
        number = int(number)
        power = int(power.lstrip('-'))

        # Вычисление значения
        power_result = 1
        for count in range(1, power + 1):
            power_result *= number
        result = 1 / power_result

        # Вывод результата
        print(result)
    else:
        print("Некорректный ввод:(")


# Вызов функции
exponentiation()
