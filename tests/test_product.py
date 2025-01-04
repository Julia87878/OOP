from src.product import Product


def test_product_init(product):
    assert product.name == "апельсины"
    assert product.description == "египетские"
    assert product.price == 30.2
    assert product.quantity == 70


def test_new_product(product_dict_first):
    product_77 = Product.new_product(product_dict_first)
    assert product_77.name == "груши"
    assert product_77.description == "Зимняя"
    assert product_77.price == 30.5
    assert product_77.quantity == 70


def test_price_update(capsys, product):
    product.price = -2
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"
    product.price = 0
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"
    product.price = 32.8
    assert product.price == 32.8


def test_product_str(product):
    assert str(product) == "апельсины, 30.2 руб. Остаток: 70 шт.\n"


def test_product_add(product, product_07):
    assert product + product_07 == 2930
