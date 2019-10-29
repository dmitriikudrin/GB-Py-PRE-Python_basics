"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной
буквы. Необходимо использовать написанную ранее функцию int_func().
"""


# Функция изменяющая первый символ в одном слове
def int_func(input_str: str):
    return input_str.title()


# Функция изменяющая первый символ в каждом слове последоательности
def int_func_seq(input_str: str):
    output_str = ''
    temp_list = input_str.split()
    for i in temp_list:
        output_str = output_str + int_func(i) + ' '
    return output_str.strip()


print(int_func("text"))
print(int_func_seq("text text text"))
