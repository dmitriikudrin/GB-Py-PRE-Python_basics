# Проверка ввода на соответсвие численному формату
def check_number(n):
    while True:
        if n.isdigit():
            return float(n)
        else:
            n = input("Неверный ввод. Необходимо ввести число - ")


# Входные данные
revenue = check_number(input("Введите выручку фирмы - "))
costs = check_number(input("Введите издержки фирмы - "))
profitability = 0
profitability_percent = 0
print()

# Вычисление рентабельности
if (revenue / costs) >= 0:
    print("Фирма работает с прибылью.")
    profitability = revenue / costs
    profitability_percent = round((profitability - 1) * 100, 2)
    print(f"Рентабильность фирмы - {profitability_percent}%")
    print()
else:
    print("Фирма работает в убыток")

"""
Из условия задания я понял, что прибыль фирмы в расчете на сотрудника
вычисляется в любом случае, независимо от рентабильности
"""
number = check_number(input("Введите количество сотрудников фирмы - "))
prof_per_employee = round(revenue / number, 2)
print(f"Прибыль фирмы в расчете на одного сотрудника - {prof_per_employee}")
