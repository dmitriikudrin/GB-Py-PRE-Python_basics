"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на
русские. Новый блок строк должен записываться в новый текстовый файл.
"""

if __name__ == "__main__":
    try:
        # Словарь для замены
        dict_num = {
            "one": "один",
            "two": "два",
            "three": "три",
            "four": "четыре"
        }
        with open("Homework#5.4-input.txt", "r", encoding="utf-8") \
                as file_input:
            with open("Homework#5.4-output.txt", "w", encoding="utf-8") \
                    as file_output:
                for line in file_input.readlines():
                    temp_list = line.split()
                    # Запись в файл с заменой числительного
                    print(f"{dict_num[temp_list[0].lower()].title()} "
                          f"{temp_list[1]} {temp_list[2]}", file=file_output)

    except IOError as e:
        print(f"Произошла ошибка в вода вывода:\n{e}:")
