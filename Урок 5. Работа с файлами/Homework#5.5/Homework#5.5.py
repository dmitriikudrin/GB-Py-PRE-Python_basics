"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.
"""

from random import random

if __name__ == "__main__":
    num_list = [int(random() * 100) for item in range(10)]
    try:
        with open("Homework#5.5.txt", "w") as file:
            for item in num_list:
                print(item, file=file)
    except IOError as e:
        print(f"Произошла ошибка в вода вывода:\n{e}:")

    num_sum = 0
    try:
        with open("Homework#5.5.txt", "r") as file:
            for line in file.readlines():
                num_sum += int(line[:-1])
    except IOError as e:
        print(f"Произошла ошибка в вода вывода:\n{e}:")
    print(f"Сумма чисел в файле - {num_sum}")

