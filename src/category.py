from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        total_count = 0
        for product in self.__products:
            total_count += product.quantity
        return f"{self.name}, количество продуктов: {total_count} шт.\n"

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}"
        return product_str

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products_in_list(self):
        return self.__products
