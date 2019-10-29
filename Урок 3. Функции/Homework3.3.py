"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def sum_of_the_two_maximum(*args):
    # Определение функции, выполняющей сложение двух наибольших элементов
    temp_list = list(args)
    return temp_list.pop(temp_list.index(max(temp_list))) + max(temp_list)


# Ввод чисел
print("Введите 3 числа:")
user_num1 = input("Введите первое число - ")
user_num2 = input("Введите второе число - ")
user_num3 = input("Введите третье число - ")

# Проверка корректности ввода и выполнение функции
if user_num1.isdigit() and user_num2.isdigit() and user_num3.isdigit():
    print(sum_of_the_two_maximum(
        int(user_num1),
        int(user_num2),
        int(user_num3)
    ))
else:
    print("Некорректный ввод:(")
