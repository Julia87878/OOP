def test_category_init(first_category, second_category):
    assert first_category.name == "Овощи"
    assert first_category.description == "краснодарские"
    assert len(first_category.products) == 4

    assert second_category.name == "Фрукты"
    assert second_category.description == "цитрусовые"
    assert len(second_category.products) == 3

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 7
    assert second_category.product_count == 7
