"""
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

if __name__ == "__main__":
    try:
        print("Введите данные построчно.\n"
              "Для окончания ввода введи пустую строку.")
        with open("Homework#5.1.txt", "w") as file:
            while True:
                temp_line = input()
                if temp_line:
                    file.write(f"{temp_line}\n")
                else:
                    break
    except IOError as e:
        print(f"Произошла ошибка в вода вывода:\n{e}:")
