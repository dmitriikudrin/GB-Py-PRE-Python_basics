"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Data:
    """Класс «Дата»"""
    def __init__(self, data):
        """Конструктор класса.
        На вход получает строку формата «день-месяц-год».
        Извлекает значения:
            day - день
            month - месяц
            year - год"""
        self.__data_list = list(map(Data.data_parse,
                                    data.split("-")))
        self.day = Data.validation(self.__data_list[0], "day")
        self.month = Data.validation(self.__data_list[1], "month")
        self.year = Data.validation(self.__data_list[2], "year")

    @classmethod
    def data_parse(cls, number):
        """Метод преобразовывания к типу «Число»"""
        try:
            return int(number)
        except ValueError as e:
            print(f"Неверный тип данных:\n{e}")

    @staticmethod
    def validation(number, num_type):
        """Метод валидации числа, месяца и года"""

        try:
            number = int(number)
        except ValueError as e:
            print(f"Неверный тип данных:\n{e}")

        # Проверка корректности введеного числа
        if num_type == "day":
            if 1 <= number <= 31:
                return number
            else:
                print("Неверное значение. Корректное значение от 1 до 31.")
        elif num_type == "month":
            if 1 <= number <= 12:
                return number
            else:
                print("Неверное значение. Корректное значение от 1 до 12.")
        elif num_type == "year":
            # Проверяем соотвествие года Нашей эре
            if 0 <= number <= 2019:
                return number
            else:
                print("Неверное значение. Корректное значение от 0 до 2019.")
        else:
            print(f"Неверное значение типа фрагмента даты - {num_type}.")


temp = Data("05-11-2019")
