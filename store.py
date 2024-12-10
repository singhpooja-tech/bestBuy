from products import Product
from typing import List, Tuple


class Store:
    def __init__(self, products: List[Product]):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(product.quantity for product in self.products)

    def get_all_products(self) -> List[Product]:
        return [product for product in self.products if product.active]

    @staticmethod
    def order(shopping_list: List[Tuple[Product, int]]) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
