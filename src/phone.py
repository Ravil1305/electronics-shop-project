from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Класс `Phone` содержит все атрибуты класса `Item` и дополнительно атрибут,
        содержащий количество поддерживаемых сим-карт. Количество физических SIM-карт
        должно быть целым числом больше нуля.
        """
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        """Геттер для number_of_sim"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, quantity_sim):
        """
        Сеттер для number_of_sim с проверкой
        на принадлежность к целым числом больше нуля"""
        if quantity_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.__number_of_sim = quantity_sim
    def __repr__(self):
        """
        Переопределение метода __repr__ родительского
        класса Item
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
