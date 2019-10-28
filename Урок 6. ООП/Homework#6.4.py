"""
Опишите несколько классов: TownCar, SportCar, WorkCar, PoliceCar. У каждого
класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также несколько методов: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
"""


class Car:
    """Класс Машина.
    Конструктор принимает:
        speed - скорость,
        color - цвет,
        name - имя,
        is_police (булево) - является ли полицией."""

    def __init__(self, speed, color, name, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self._is_police = is_police

    def go(self):
        """Метод, приводящий машину в движение."""
        print("Машина поехала.")

    def stop(self):
        """Метод, останавливающий машину."""
        print("Машина остановилась.")

    def turn(self, direction):
        """Метод, заставляющий машину повернуть.
        Принимает direction."""
        print(f"Машина повернула {direction}.")


class TownCar(Car):
    """Класс TownCar. На базе класса Car"""

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class SportCar(Car):
    """Класс SportCar. На базе класса Car"""

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    """Класс WorkCar. На базе класса Car"""

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class PoliceCar(Car):
    """Класс PoliceCar. На базе класса Car"""

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._is_police = True


