def test_category_init(first_category, second_category, third_category):
    assert first_category.name == "Овощи"
    assert first_category.description == "краснодарские"
    assert len(first_category.products) == 4

    assert second_category.name == "Фрукты"
    assert second_category.description == "цитрусовые"
    assert len(second_category.products) == 3

    assert third_category.name == "Хлебобулочные изделия"
    assert third_category.description == "батоны"
    assert len(third_category.products) == 0

    assert first_category.category_count == 3
    assert second_category.category_count == 3
    assert third_category.category_count == 3

    assert first_category.product_count == 7
    assert second_category.product_count == 7
    assert third_category.product_count == 7
