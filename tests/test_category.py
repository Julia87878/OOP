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
