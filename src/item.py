import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """
        Геттер для `name`.
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        В сеттере `name` проверяем, что длина наименования товара не больше 10 символов.
        """
        if len(name) > 10:
            raise ValueError("Длина наименования товара превышает 10 символов.")
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls, data_file='../src/items.csv'):
        """
        Класс-метод, инициализирующий экземпляры
        класса `Item` данными из файла _src/items.csv_
        """
        with open(data_file, encoding='windows-1251') as file:
            reader = csv.DictReader(file)
            for data in reader:
                cls.all.append((data['name'], float(data['price']), int(data['quantity'])))

    @staticmethod
    def string_to_number(number):
        """
        Статический метод, возвращающий число из числа - строки
        """
        return int(number.split(".")[0])

    def __repr__(self):
        """Метод __repr__"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Метод __str__"""
        return f"{self.__name}"

    def __add__(self, other):
        """
        Cложение экземпляров класса `Phone` и `Item` (сложение по количеству товара в магазине)
        с проверкой, чтобы нельзя было сложить `Phone` или `Item` с экземплярами не `Phone`
        или `Item` классов.
        """
        if not isinstance(other, Item):
            raise TypeError('Нельзя сложить `Phone` или `Item` с экземплярами не `Phone` или `Item` классов')
        return self.quantity + other.quantity
