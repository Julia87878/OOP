def test_product_init(product):
    assert product.name == "апельсины"
    assert product.description == "египетские"
    assert product.price == 30.2
    assert product.quantity == 70
