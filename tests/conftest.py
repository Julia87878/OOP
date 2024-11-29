import pytest

from src.category import Category
from src.product import Product


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
def product():
    return Product("апельсины", "египетские", 30.2, 70)
