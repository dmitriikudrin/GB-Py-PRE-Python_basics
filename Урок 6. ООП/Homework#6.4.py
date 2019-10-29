"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).  А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите
результат.
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

    def show_speed(self):
        """Метод, показывающий текущую скорость автомобиля."""
        print(f"Текущая скорость автомобиля {self.speed} км/ч.")


class TownCar(Car):
    """Класс TownCar. На базе класса Car"""

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        """Переопределение метода.
        Метод, показывающий текущую скорость автомобиля."""
        if self.speed <= 60:
            print(f"Текущая скорость автомобиля {self.speed} км/ч.")
        else:
            print(f"Текущая скорость автомобиля {self.speed} км/ч.\n"
                  f"Превышение скорости. Разрешенная скорость 60 км/ч.")


class SportCar(Car):
    """Класс SportCar. На базе класса Car"""

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    """Класс WorkCar. На базе класса Car"""

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        """Переопределение метода.
        Метод, показывающий текущую скорость автомобиля."""
        if self.speed <= 40:
            print(f"Текущая скорость автомобиля {self.speed} км/ч.")
        else:
            print(f"Текущая скорость автомобиля {self.speed} км/ч.\n"
                  f"Превышение скорости. Разрешенная скорость 40 км/ч.")


class PoliceCar(Car):
    """Класс PoliceCar. На базе класса Car"""

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._is_police = True


# Проверка
car_dict = {
    "TownCar": TownCar(100, "black", "toyota"),
    "SportCar": SportCar(100, "white", "bmw"),
    "WorkCar": WorkCar(50, "blue", "nissan"),
    "PoliceCar": PoliceCar(200, "yellow", "skoda")
}

for key, value in car_dict.items():
    print(key)
    value.go()
    value.stop()
    value.turn("налево")
    value.show_speed()
    print()

