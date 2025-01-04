from src.baseproduct import BaseProduct
from src.printmixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n"

    def __add__(self, other):
        if type(other) is Product:
            result = self.__price * self.quantity + other.price * other.quantity
            return result
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product_dict: dict):
        return cls(**product_dict)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_priсe: float):
        if new_priсe <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_priсe
