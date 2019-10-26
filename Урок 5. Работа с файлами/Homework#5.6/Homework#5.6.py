"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает
учебный предмет и наличие лекционных, практических и лабораторных занятий по
этому предмету и их количество. Важно, чтобы для каждого предмета не
обязательно были все типы занятий. Сформировать словарь, содержащий название
предмета и общее количество занятий по нему. Вывести словарь на экран.
"""

# Понимаю, что намудрил в решении, но пока не знаю как сделать по другому

sub_dict = dict()

if __name__ == "__main__":
    try:
        with open("Homework#5.6.txt", "r", encoding="utf-8") as file:
            for line in file.readlines():
                line_list = line.split()
                sub_dict[line_list[0]] = 0

                # Формирование суммарной информации о дисциплине для вывода
                print_line = f"{line_list[0]}:"
                if int(line_list[1]):
                    print_line += f" {line_list[1]} лекций"
                    sub_dict[line_list[0]] += int(line_list[1])
                if int(line_list[2]):
                    print_line += f" {line_list[2]} практических занятий"
                    sub_dict[line_list[0]] += int(line_list[2])
                if int(line_list[3]):
                    print_line += f" {line_list[3]} лабораторных занятий"
                    sub_dict[line_list[0]] += int(line_list[3])
                if not int(line_list[1]) and \
                        not int(line_list[2]) and \
                        not int(line_list[3]):
                    print_line += f" зазанятий нет"
                print(print_line)

            # Вывод сводной информации по предметам
            print("\nСводная информации по предметам:")
            for key, value in sub_dict.items():
                print(f"Количество занятий по предмету \"{key}\" - {value}")
    except IOError as e:
        print(f"Произошла ошибка в вода вывода:\n{e}:")
