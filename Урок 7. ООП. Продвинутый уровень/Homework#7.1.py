"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init__()), который должен принимать данные (список списков) для
формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных
в виде прямоугольной схемы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы
в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки второй
матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self._matrix = matrix

        # Вычисление размера матрицы и длины максимального элемента матрицы
        self.num_line = len(self._matrix)
        self.num_column = 0
        self.__max_len_el = 0
        for line in self._matrix:
            if len(line) > self.num_column:
                self.num_column = len(line)
            for el in line:
                if len(str(el)) > self.__max_len_el:
                    self.__max_len_el = len(str(el))

        # Заполнение 0 недостающих элементов матрицы
        for line in self._matrix:
            while True:
                if len(line) == self.num_line:
                    break
                line.append(0)

    def __str__(self):
        """Переопределение метода __str__ для матрицы"""
        temp_list = []
        for line in self._matrix:
            form_str = "{0:>" + str(self.__max_len_el + 1) + "}"
            temp_list.append(
                ' '.join([form_str.format(str(el)) for el in line])
            )
        return '\n'.join(temp_list)

    def __add__(self, other):
        """Переопределение метода сложения матриц"""
        # Проверка на равенство размеров матриц
        if self.num_line == other.num_line and \
                self.num_column == other.num_column:
            temp_list = []  # временный список с элементами матрицы
            for i in range(self.num_line):
                temp_line = []  # временный список с элементами строки матрицы
                for j in range(self.num_column):
                    temp_line.append(self._matrix[i][j] + other._matrix[i][j])
                temp_list.append(temp_line)
            return Matrix(temp_list)    # Создание новой матрицы
        else:
            # Присваивание новой матрицы значения None и вывод предупреждения
            # при неравестве размеров матрицы
            print("Различный размер матриц.")
            return None


mat1 = Matrix([[1, 2], [3, 4]])
mat2 = Matrix([[5, 6], [7, 8]])
mat3 = mat1 + mat2

print(mat1)
print(mat2)
print(mat3)
