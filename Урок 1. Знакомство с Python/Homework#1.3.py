# Входные данные
number = input("Введите число - ")
while True:
    if number.isdigit():
        break
    else:
        number = input("Неверный ввод. Необходимо ввести целое число - ")

max_num = 0

for i in number:
    if int(i) > max_num:
        max_num = int(i)

# Вывод результата
print()
print(f"В числе {number} наибольшая цифра - {max_num}")
