"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color
(цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках
метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Время перехода между режимами должно составлять 7 и 2 секунды. Проверить работу
примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep


class TrafficLight:
    # Цвет в текущий момент
    __color = None
    # Варианты цветов
    __colors = ["red", "yellow", "green", "yellow"]

    # Метод переключения цвета
    def running(self, count=10):

        # Переключение цвета
        for i in range(count):
            for color in self.__colors:

                # Определние цвета
                self.__color = color

                # Определение времени переключения
                if color == "red" or color == "green":
                    timing = 7
                elif color == "yellow":
                    timing = 2

                # Вывод цвета с обратным отсчетом
                for j in range(timing, 0, -1):
                    line = f"\r{self.__color} {j}"
                    print(line, end="")
                    sleep(1)


# СОздание экземпляра и вызов метода
my_TrafficLight = TrafficLight()
my_TrafficLight.running()
