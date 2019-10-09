# Входные данные
n = input("Введите число n - ")
while True:
    if n.isdigit():
        break
    else:
        n = input("Неверный ввод. Необходимо ввести целое число - ")

# Вывод результата
print()
print(f"Сумма n + nn + nnn - {int(n) + int(n * 2) + int(n * 3)}")
