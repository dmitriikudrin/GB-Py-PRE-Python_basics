"""
Пользователь вводит время в секундах. Переведите время в часы, минуты и
секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

print("Для выхода из программы введите exit.")
user_data = input("Введите время в секундах - ")
while True:
    # Условие выхода из цикла
    if user_data.lower() == "exit":
        print("Работа программы завершена.")
        break
    #
    elif user_data.isdigit():
        # Вычисление резульатата
        user_data = int(user_data)
        hours = user_data // 3600
        minutes = (user_data % 3600) // 60
        seconds = user_data % 60
        # Вывод результата
        print()
        print("Итоговое время:")
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        break
    # Повторный ввод в случае неверного ввода
    else:
        user_data = input("Неверный ввод. Необходимо ввести целое число - ")


