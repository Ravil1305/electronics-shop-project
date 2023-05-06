"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.class_error import InstantiateCSVError
from src.item import Item
from src.phone import Phone


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


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


def test_instantiate_from_csv(tmp_path):
    """Тестирует метод instantiate_from_csv."""
    csv_data = "name,price,quantity\nproduct,10.0,5"
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_data)

    # Вызываем метод instantiate_from_csv() с временным файлом
    Item.instantiate_from_csv(data_file=csv_file)
    assert len(Item.all[0].name) == 8
    assert len(Item.all) == 4


def test_instantiate_from_csv_with_InstantiateCSVError(tmp_path):
    csv_data = 'name,price\nitem1,10.0\nitem2,20.0\n'
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_data)

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(data_file=csv_file)


def test_instantiate_from_csv_with_FileNotFoundError():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(data_file='none_file.csv')


def test_len_name_setter(item1):
    """Тестирует сеттер  self.__name."""
    with pytest.raises(ValueError):
        item1.name = 'СуперСмартфон'
    item1.name = "Смартфон"


def test_string_to_number(item1):
    """Тестирует метод string_to_number."""
    assert item1.string_to_number("10000") == 10000
    assert item1.string_to_number("2.034") == 2


def test_repr(item1):
    """Тестирует метод repr."""
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str(item1):
    """Тестирует метод str."""
    assert str(item1) == 'Смартфон'


def test_add(item1, phone1):
    """Тестирует сложение экземпляров с проверкой на TypeError"""
    with pytest.raises(TypeError):
        item1 + 5
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
