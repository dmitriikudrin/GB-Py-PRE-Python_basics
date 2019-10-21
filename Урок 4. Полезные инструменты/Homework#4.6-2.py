"""
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного
заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""

# Данный скрипт бесконечно повторяет элементы некоторого списка, определенного
# заранее.
# Размер списка задается из консоли. (По умолчанию 10)

from itertools import cycle
from sys import argv
from time import sleep
from random import random

# Проверка наличия начального значения
if len(argv) == 1:
    num_elem = 10
else:
    num_elem = int(argv[1])

# Генератор начального списка
input_list = [int(random() * 100) for i in range(0, num_elem)]
print("Исходный список:")
print(*input_list)

# Генератор бесконечного цикла
for el in cycle(input_list):
    print(el)
    sleep(0.5)
