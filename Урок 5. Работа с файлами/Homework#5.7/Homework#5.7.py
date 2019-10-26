"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором
каждая строка должна содержать данные о фирме:
название, форма собственности,выручка, издержки.

Пример строки файла: firm_1   ООО   10000   5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить
ее в словарь (со значением убытков).

Пример списка:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000},
{"average_profit": 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Подсказка: использовать менеджер контекста.
"""

import json

# Инициализация итогового списка
stats_list = [dict(), {"average_profit": 0}]

if __name__ == "__main__":
    # Чтение и обработка файла
    try:
        with open("Homework#5.7-input.txt", "r", encoding="utf-8") as file:
            profit_count = 0
            profit_sum = 0
            for line in file.readlines():
                firm_list = line.split()
                profit = int(firm_list[2]) - int(firm_list[3])
                stats_list[0][firm_list[0]] = profit
                if profit >= 0:
                    profit_count += 1
                    profit_sum += profit

            # Вычисление средней прибыли
            try:
                stats_list[1]["average_profit"] = profit_sum // profit_count
            except ZeroDivisionError:
                stats_list[1]["average_profit"] = "Нет фирм с прибылью"
            print(stats_list)
    except IOError as e:
        print(f"Произошла ошибка в вода вывода:\n{e}:")

    # Запись файла JSON
    try:
        with open("Homework#5.7-output.json", "w", encoding="utf-8") as file:
            json.dump(stats_list, file)

    except IOError as e:
        print(f"Произошла ошибка в вода вывода:\n{e}:")
