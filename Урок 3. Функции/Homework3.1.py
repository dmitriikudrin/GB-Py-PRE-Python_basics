"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.
"""


def my_division(dividend, divider):
    # Определение функции, выполняющей деление 2 чисел
    if divider == 0:
        print("Делить на ноль нельзя:(")
    else:
        print(f"Результат деления {dividend} на {divider} равен "
              f"{dividend / divider}")


# Ввод чисел
print("Введите 2 числа:")
user_number_1 = input("Введите первое число - ")
user_number_2 = input("Введите второе число - ")

# Проверка корректности ввода и выполнение функции
if user_number_1.isdigit() and user_number_2.isdigit():
    my_division(int(user_number_1), int(user_number_2))
else:
    print("Некорректный ввод:(")
