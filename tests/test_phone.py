import pytest
from src.phone import Phone


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_phone1_init(phone1):
    """Тестирует метод init."""
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2


def test_number_of_sim_setter(phone1):
    """Тестирует сеттер __number_of_sim"""
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
    phone1.number_of_sim = 2


def test_repr(phone1):
    """Тестирует переопределенный метод repr."""
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
