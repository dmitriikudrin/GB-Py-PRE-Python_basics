"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем
атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
“Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать
экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:
    """Класс Stationery.
    Конструктор принимает:
        title"""
    def __init__(self, title):
        self.title = title

    def draw(self):
        """Метод отрисовки"""
        print("Запуск отрисовки.")


class Pen(Stationery):
    """Класс Pen. На базе класса Stationery"""
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        """Переопределение метода отрисовки"""
        print(f"Запуск отрисовки ручки {self.title}.")


class Pencil(Stationery):
    """Класс Pencil. На базе класса Stationery"""
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        """Переопределение метода отрисовки"""
        print(f"Запуск отрисовки карандаша {self.title}.")


class Handle(Stationery):
    """Класс Handle. На базе класса Stationery"""
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        """Переопределение метода отрисовки"""
        print(f"Запуск отрисовки маркера {self.title}.")


# Создание экземпляров классов и выполнения метода
my_stationery = Stationery("My Stationery")
my_stationery.draw()

my_pen = Pen("My Pen")
my_pen.draw()

my_pencil = Pencil("My Pencil")
my_pencil.draw()

my_handle = Handle("My Handle")
my_handle.draw()
