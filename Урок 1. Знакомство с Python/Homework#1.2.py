"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""


# Входные данные
print("Для выхода из программы введите exit.")
user_number = input("Введите число n - ")

while True:
    # Условие выхода из цикла
    if user_number.lower() == "exit":
        print("Работа программы завершена.")
        break
    #
    elif user_number.isdigit():
        user_number = int(user_number)
        # Вывод результата
        print()
        print(f"Сумма n + nn + nnn - "
              f"{user_number + user_number * 2 + user_number * 3}")
        break
    else:
        user_number = input("Неверный ввод. Необходимо ввести целое число - ")


