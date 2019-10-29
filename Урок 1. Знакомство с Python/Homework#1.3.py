"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""


# Входные данные
print("Для выхода из программы введите exit.")
user_number = input("Введите целое число - ")

while True:
    # Условие выхода из цикла
    if user_number.lower() == "exit":
        print("Работа программы завершена.")
        break
    # Выполнение программы
    elif user_number.isdigit():
        max_num = 0
        for i in user_number:
            if int(i) > max_num:
                max_num = int(i)
        # Вывод результата
        print()
        print(f"В числе {user_number} наибольшая цифра - {max_num}")
        break
    else:
        user_number = input("Неверный ввод. Необходимо ввести целое число - ")