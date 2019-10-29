"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

# Списки времен года и соотвествующие ему месяца
month_winter = [12, 1, 2]
month_spring = [3, 4, 5]
month_summer = [6, 7, 8]
month_autumn = [9, 10, 11]

# Ввод пользователем номера месяца
user_number = input("Введите месяц в виде целого числа от 1 до 12 - ")

# Проверка корректности ввода пользователем
if user_number.isdigit():
    # Если ввод корректный.
    # Вывод времени года соответствующему номеру месяца
    user_number = int(user_number)
    if user_number in month_autumn:
        user_season = "Зима"
    elif user_number in month_spring:
        user_season = "Весна"
    elif user_number in month_summer:
        user_season = "Лето"
    else:
        user_season = "Осень"
    print(f"Месяц №{user_number} относится к времени года - "
          f"{user_season}")
else:
    # Если ввод некорректный
    print("Вы ввели не число. Необходимо ввести число.")





