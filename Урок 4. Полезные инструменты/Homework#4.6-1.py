"""
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного
заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""

# Данный скрипт бесконечно генерирует целые числа начиная с указзанного
# значения через каждые 0.5 секунд
# Значение задается в виде аргумента консоли (По умолчанию с 1)

from itertools import count
from sys import argv
from time import sleep

# Проверка наличия начального значения
if len(argv) == 1:
    start = 1
else:
    start = int(argv[1])

# Генератор бесконечного цикла
for el in count(start):
    print(el)
    sleep(0.5)
