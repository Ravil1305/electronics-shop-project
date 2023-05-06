class InstantiateCSVError(Exception):
    """Класс-исключение `InstantiateCSVError`"""

    def __init__(self, *args) -> None:
        self.message = args[0] if args else "_Файл items.csv поврежден_"

    def __str__(self) -> str:
        return self.message
