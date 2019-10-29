"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
натуральных чисел. У пользователя необходимо запрашивать новый элемент
рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2. Пользователь
ввел число 3. Результат: 7, 5, 3, 3, 3, 2. Пользователь ввел число 8.
Результат: 8, 7, 5, 3, 3, 2. Пользователь ввел число 1.
Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
"""

from copy import deepcopy

user_list = []
print("Необходимо вводить натуральные числа по одному.\n"
      "Для завершения работы введите exit.\n")

while True:
    # Ввод пользователем числа
    user_element = input("Введите натуральное число - ")

    # Проверяем корректность ввод и условие завершения программы
    if user_element == "Exit" or user_element == "exit":
        # Условие завершения программы
        print("\nРабота программы завершена.")
        print(f"Итоговый список:\n{user_list}")
        break

    # Добавление элемента в список
    elif user_element.isdigit():
        user_element = int(user_element)
        # Добавление в список первого элемента
        if len(user_list) == 0:
            user_list.append(user_element)
        # Добавление в список уже существующего элемента
        elif user_element in user_list:
            user_list.insert(user_list.index(user_element), user_element)
        # Добавление в список уникального элемента
        else:
            # Создание временной копии списка
            temp_list = deepcopy(user_list)
            # Создание временной позиции нового элемента
            temp_element_index = 0
            # Нахождение позиции нового элемента
            for i in temp_list:
                if user_element > i:
                    temp_element_index = temp_list.index(i)
                    break
                else:
                    temp_element_index = len(temp_list)
            # Добавление нового элемента
            user_list.insert(temp_element_index, user_element)

        # Вывод промежуточного списка
        print(user_list)

    else:
        # Уведомление пользователя о неправльном вводе
        print("Вы ввели не число.")
