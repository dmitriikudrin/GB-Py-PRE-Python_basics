number = input("Введите число - ")
max_num = 0

for i in number:
    if int(i) > max_num:
        max_num = int(i)

print(f"В числе {number} наибольшая цифра - {max_num}")
