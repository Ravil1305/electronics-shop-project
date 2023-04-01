"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_item_init(item1):
    """Тестирует метод init."""
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20


def test_calculate_total_price(item1):
    """Тестирует метод calculate_total_price."""
    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):
    """Тестирует метод apply_discount."""
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000


def test_instantiate_from_csv(item1):
    """Тестирует метод instantiate_from_csv."""
    Item.instantiate_from_csv(data_file='./src/items.csv')
    assert len(Item.all[0].name) == 8
    assert len(Item.all) == 9


def test_len_name_setter(item1):
    """Тестирует сеттер  self.__name."""
    with pytest.raises(ValueError):
        item1.name = 'СуперСмартфон'
    item1.name = "Смартфон"


def test_string_to_number(item1):
    """Тестирует метод string_to_number."""
    assert item1.string_to_number("10000") == 10000
    assert item1.string_to_number("2.034") == 2
