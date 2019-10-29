"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

if __name__ == "__main__":
    try:
        with open("Homework#5.2.txt", "r", encoding="utf-8") as file:
            line_count = 0
            words_count = 0
            for line in file:
                line_count += 1
                line_len = len(line.split())
                words_count += line_len
                print(f"Строка №{line_count} (слов в строке: {line_len}) - "
                      f"{line[:-1]}")
            print(f"Всего строк в файле - {line_count}.")
            print(f"Всего слов в файле - {words_count}.")
    except IOError as e:
        print(f"Произошла ошибка в вода вывода:\n{e}:")
