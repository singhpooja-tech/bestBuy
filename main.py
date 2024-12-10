from products import Product
from store import Store


def main():
    # Create a list of products
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]


# Initialize the store with the product list
    store = Store(product_list)

    # Get all active products
    products = store.get_all_products()

    # Print the total quantity of products in store
    print(store.get_total_quantity())

    # Place an order with 1 MacBook Air M2 and 2 Bose QuietComfort Earbuds
    total_price = store.order([(products[0], 1), (products[1], 2)])
    print(f"Total price for the order: {total_price}")


if __name__ == "__main__":
    main()
