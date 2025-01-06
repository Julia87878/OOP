import pytest


def test_category_init(first_category, second_category, third_category):
    assert first_category.name == "Овощи"
    assert first_category.description == "краснодарские"
    assert len(first_category.products_in_list) == 4

    assert second_category.name == "Фрукты"
    assert second_category.description == "цитрусовые"
    assert len(second_category.products_in_list) == 3

    assert third_category.name == "Хлебобулочные изделия"
    assert third_category.description == "батоны"
    assert len(third_category.products_in_list) == 0

    assert first_category.category_count == 3
    assert second_category.category_count == 3
    assert third_category.category_count == 3

    assert first_category.product_count == 7
    assert second_category.product_count == 7
    assert third_category.product_count == 7


def test_category_products_property(second_category):
    assert second_category.products == (
        "апельсины, 30.2 руб. Остаток: 70 шт.\nмандарины, 10.5 руб. Остаток: 100 шт.\n"
        "лимоны, 20.8 руб. Остаток: 40 шт.\n"
    )


def test_add_product(first_category, product_07):
    first_category.add_product(product_07)
    assert first_category.products == (
        "помидоры, 40.7 руб. Остаток: 50 шт.\nогурцы, 20.5 руб. Остаток: 30 шт.\n"
        "морковь, 10.4 руб. Остаток: 25 шт.\nперец, 50.5 руб. Остаток: 35 шт.\n"
        "кабачки, 10.2 руб. Остаток: 80 шт.\n"
    )


def test_category_str(second_category):
    assert str(second_category) == "Фрукты, количество продуктов: 210 шт.\n"


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "апельсины"
    assert next(product_iterator).name == "мандарины"
    assert next(product_iterator).name == "лимоны"

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_category_add_product_error(first_category):
    with pytest.raises(TypeError):
        assert first_category.add_product(1) == TypeError


def test_middle_product_price(first_category, third_category):
    assert first_category.middle_price() == 30.53
    assert third_category.middle_price() == 0
