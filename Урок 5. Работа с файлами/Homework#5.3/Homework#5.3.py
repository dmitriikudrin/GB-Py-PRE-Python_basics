"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов. Определить, кто из сотрудников имеет оклад менее
20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников.
"""

if __name__ == "__main__":
    try:
        with open("Homework#5.3.txt", "r", encoding="utf-8") as file:
            # Счетчик числа сотрудников
            emp_count = 0
            # Общий оклад всех сотрудников
            # (требуется вычисления средней зарплаты)
            emp_sum = 0
            # Список сотрудников, чей оклад меньше 20 тыс.
            emp_less20 = []

            # Вывод списка всех сотрудников
            print("Список сотрудников:")
            for idx, line in enumerate(file):
                emp = line.split()
                emp_count += 1
                emp_salary = int(emp[1])
                emp_sum += emp_salary

                # Вывод информации о сотруднике
                print(f"{emp_count}: {emp[0]} - {emp_salary}")

                # Проверка оклада и отсевание сотрудников
                if emp_salary < 20000:
                    emp_less20.append(emp)
            print(f"\nВсего сотрудников: {emp_count}")

            # Средння зарплата всех сотрудников
            average_salary = emp_sum // emp_count
            print(f"Средння зарплата всех сотрудников: {average_salary}")

            # Вывод сотрудников, чей оклад меньше 20 тыс.
            if len(emp_less20) != 0:
                print("\nСписок сотрудников, чей оклад меньше 20 тыс.:")
                for idx, item in enumerate(emp_less20, start=1):
                    print(f"{idx}: {item[0]}: {item[1]}")
    except IOError as e:
        print(f"Произошла ошибка в вода вывода:\n{e}:")
