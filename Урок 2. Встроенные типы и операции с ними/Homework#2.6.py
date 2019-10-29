"""
*Реализовать структуру данных «Товары». Она должна представлять собой список
кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже
должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у
пользователя. Пример готовой структуры:
[
    (1, {“название”: “компьютер”,“цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый
ключ — характеристика товара, например название, а значение — список
значений-характеристик, например список названий товаров.
Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000], “количество”: [5, 2, 7], “ед”: [“шт.”]
}
"""

from copy import deepcopy

# Шаблон структуры товара
product_structure = [
    "number", {
        "name": "product_name",
        "price": "product_price",
        "quantity": "product_quantity",
        "unit": "product_unit"
    }
]

# Сумарная структура товаров
summary_product_structure = []

# Структура статистики товаров
statistics_structure = {
    "name": [],
    "price": [],
    "quantity": [],
    "unit": []
}

print("Заполните информацию о каждом товаре.")

# Начальное значение номера товара равно 1
number = 1

while True:
    # Временная структура с вводимым товаром
    temp_product = deepcopy(product_structure)

    # Заполнение информации о товаре
    temp_product[0] = number
    temp_product[1]["name"] = input("Введите название товара - ")
    temp_product[1]["price"] = input("Введите цену товара - ")
    temp_product[1]["quantity"] = input("Введите количество товара - ")
    temp_product[1]["unit"] = input("Введите единицу измерения товара - ")

    # Добавление временной позиции в кортеж товаров
    summary_product_structure.append(tuple(temp_product))

    # Опрос пользователя на необходимость добавления еще одного товара
    next_step = input("\nДобавить еще один товар? "
                      "Введите да или нет - ").lower()
    while next_step != "нет" or next_step != "да":
        if next_step == "нет" or next_step == "да":
            break
        else:
            next_step = input(
                "Некоректный ввод. Введите да или нет - ").lower()
    if next_step == "нет":
        break

    # Изменение номера товара для последующего ввода
    number += 1
    print()

# Формирование статистики товаров
for i in summary_product_structure:
    statistics_structure["name"].append(i[1]["name"])
    statistics_structure["price"].append(i[1]["price"])
    statistics_structure["quantity"].append(i[1]["quantity"])
    statistics_structure["unit"].append(i[1]["unit"])

# Вывод статистики товаров
user_decision = input("\nВывести сумарную статистику товаров? "
                      "Введите да или нет - ").lower()
while user_decision != "нет" or user_decision != "да":
    if user_decision == "нет" or user_decision == "да":
        break
    else:
        user_decision = input(
            "Некоректный ввод. Введите да или нет - ").lower()
if user_decision == "да":
    for i in summary_product_structure:
        print(f"№{i[0]}. Наименование - {i[1]['name']}. "
              f"Цена - {i[1]['price']}. "
              f"Количество - {i[1]['quantity']}. "
              f"Единица измерения - {i[1]['unit']}.")
