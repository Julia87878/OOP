import os

import pytest

from src.category import Category
from src.product import Product
from src.productiterator import ProductIterator


@pytest.fixture
def first_category():
    return Category(
        name="Овощи",
        description="краснодарские",
        products=[
            Product("помидоры", "желтые", 40.7, 50),
            Product("огурцы", "длинноплодные", 20.5, 30),
            Product("морковь", "крупная", 10.4, 25),
            Product("перец", "красный", 50.5, 35),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Фрукты",
        description="цитрусовые",
        products=[
            Product("апельсины", "египетские", 30.2, 70),
            Product("мандарины", "абхазские", 10.5, 100),
            Product("лимоны", "турецкие", 20.8, 40),
        ],
    )


@pytest.fixture
def third_category():
    return Category(name="Хлебобулочные изделия", description="батоны", products=[])


@pytest.fixture
def product():
    return Product("апельсины", "египетские", 30.2, 70)


@pytest.fixture
def product_07():
    return Product("кабачки", "молодые", 10.2, 80)


@pytest.fixture
def product_dict_first():
    return {"name": "груши", "description": "Зимняя", "price": 30.5, "quantity": 70}


@pytest.fixture
def path_name():
    path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "products.json")
    return path_to_file


@pytest.fixture
def product_iterator(second_category):
    return ProductIterator(second_category)
