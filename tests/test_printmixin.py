from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys):
    Product("апельсины", "египетские", 30.2, 70)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(апельсины, египетские, 30.2, 70)"

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"

    LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава 2, Выносливая трава, 450.0, 15)"
