"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"profit": profit, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_full_profit). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""


class Worker:
    """Класс Сотрудник.
    Конструктор принимает:
        name - имя,
        surname - фамилия,
        position - должность,
        profit (необязательно) - оклад,
        bonus (необязательно) - премия."""

    def __init__(self, name, surname, position, profit=0, bonus=0):
        """Конструктор класса"""
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": profit, "bonus": bonus}


class Position(Worker):
    """Класс Должность. На базе класса Worker"""

    def get_full_name(self):
        """Метод получения полного имени сотрудника"""
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        """Метод получения полного дохода сотрудника"""
        return self._income["profit"] + self._income["bonus"]

    def get_position(self):
        """Метод получения должности сотрудника"""
        return self.position


# Экземпляр класса
engineer = Position("Ivan", "Petrov", "engineer", 1000, 200)
print(engineer.get_full_name())
print(engineer.get_position())
print(engineer.get_full_profit())
