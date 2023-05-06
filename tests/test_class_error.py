from src.class_error import InstantiateCSVError


def test_class_error():
    error_message = "_Файл item.csv поврежден_"
    error = InstantiateCSVError(error_message)
    assert str(error) == error_message
