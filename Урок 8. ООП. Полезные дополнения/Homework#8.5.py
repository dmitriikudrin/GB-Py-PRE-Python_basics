"""
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании. Для
хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.
"""


class Store:
    """Класс склад."""
    length = 0                  # Длина склада
    width = 0                   # Ширина склада
    area = length * width       # Площадь склада
    address = None              # Адресс склада
    balance = {}                # Структура для учета товаров на складе

    def __init__(self, name):
        """Конструктор класса. Принимает на вход:
            name - название склада"""
        self.name = name        # Название склада

    def take_to(self, item):
        """Метод постановки на баланс склада оргтехники.
        Принимает на вход ссылку на экзмепляр класса"""
        """Проверяем налчие такой тип оргтехники на складе"""
        if f"num_{item.item_class}" in self.balance:
            # Если такой тип есть, то увеличиваем итогове кол-во на 1
            # и добавляем конкретный экземпляр на склад
            self.balance[f"num_{item.item_class}"][0] += 1
            self.balance[f"num_{item.item_class}"][1].append(
                (item.inst_name, item.vendor, item.model))
            # Делаем пометку в конкретном экзмепляре об учете на складе
            item.location = f"Склад {self.name}"
        else:
            # Если такого типа нет, то добавлеем в формате:
            # {"num_<тип_техники>":
            #               [итоговое_кол-во, [(производитель, модель), ]]}
            self.balance[f"num_{item.item_class}"] = \
                [1, [(item.inst_name, item.vendor, item.model), ]]
            # Делаем пометку в конкретном экзмепляре об учете на складе
            item.location = f"Склад {self.name}"

    def write_off(self, item, new_location):
        """Метод снятия с баланса склада оргтехники.
        Принимает на вход ссылку на экзмепляр класса и новое местоположение"""
        done_del = False
        # Находим запись об конкретном экзепляре и удаляем ее
        for temp_tuple in self.balance[f"num_{item.item_class}"][1]:
            if item.inst_name in temp_tuple:
                self.balance[f"num_{item.item_class}"][1].remove(temp_tuple)
                self.balance[f"num_{item.item_class}"][0] -= 1
                done_del = True
        if done_del:
            # Делаем пометку в конкретном экзмепляре об учете на складе
            item.location = new_location
        else:
            print("На складе не числится. Повторите попытку.")


class OfficeEquipment:
    """Базовый класс Оргтехника"""
    location = None             # Подразделение, на которм числится

    def __init__(self, vendor, model):
        """Конструктор класса. Принимает на вход:
            vendor - производитель
            model - модель"""
        self.vendor = vendor    # Производитель
        self.model = model      # Модель

    @property
    def item_class(self):
        ""
        return type(self).__name__

    @property
    def inst_name(self):
        """Свойство, которое возвращает имя экзмепляра"""
        for k, v in globals().items():
            if v == self:
                return k


class Printer(OfficeEquipment):
    """Класс Принтер. На базе класса Оргтехника."""
    def __init__(self, vendor, model, color):
        """Конструктор класса. Наследует все атрибуты от класса Оргтехника.
        Принимает на вход:
            color - Тип печати: цветной или ч/б"""
        super().__init__(vendor, model)
        self.color = color      # Тип печати: цветной или ч/б


class Scanner(OfficeEquipment):
    """Класс Сканер. На базе класса Оргтехника."""
    def __init__(self, vendor, model, dpi):
        """Конструктор класса. Наследует все атрибуты от класса Оргтехника.
        Принимает на вход:
            dpi - Оптическое разрешение сканера"""
        super().__init__(vendor, model)
        self.dpi = dpi          # Оптическое разрешение сканера


class Xerox(OfficeEquipment):
    """Класс Ксерокс. На базе класса Оргтехника."""
    def __init__(self, vendor, model, speed):
        """Конструктор класса. Наследует все атрибуты от класса Оргтехника.
        Принимает на вход:
            speed - корость копировани"""
        super().__init__(vendor, model)
        self.speed = speed      # Скорость копирования


print(1)