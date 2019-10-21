"""
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для
формирования списка использовать генератор.
"""

import random


# Генератор случайного списка из заданного количества элементов
def list_generator(stop):
    for num in range(stop):
        yield int(random.random() * 100)


# Формирование списков
input_list = list(list_generator(10))
output_list = list(input_list[i] for i in range(1, len(input_list))
                   if input_list[i] > input_list[i - 1])

# Вывод результата
print("Исходный список:")
print(*input_list)
print("Измененный список:")
print(*output_list)
