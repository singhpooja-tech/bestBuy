from products import Product
from store import Store

# Setup initial stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
]
best_buy = Store(product_list)


def start(store: Store):
    """
    Starts the user interface for the store.
    Args:
        store (Store): The store object containing products.
    """
    while True:
        print("\nWelcome to Best Buy Store!")
        print("Please select an option:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            # List all products
            print("\nAvailable Products:")
            for product in store.get_all_products():
                print(product.show())

        elif choice == "2":
            # Show total quantity in store
            total_quantity = store.get_total_quantity()
            print(f"\nTotal items in store: {total_quantity}")

        elif choice == "3":
            # Make an order
            print("\nEnter your order:")
            print("Select products by entering their number (e.g., 1 for the first product).")

            # Display all active products with an index
            products = store.get_all_products()
            for i, product in enumerate(products, start=1):
                print(f"{i}. {product.show()}")

            print("Enter the products you want to buy as 'product_number quantity'.")
            print("For example: '1 3' means buy 3 units of product 1.")
            print("Enter 'done' when you are finished.")

            shopping_list = []
            while True:
                order_input = input("Enter product and quantity: ").strip()
                if order_input.lower() == "done":
                    break

                try:
                    product_num, quantity = map(int, order_input.split())
                    if 1 <= product_num <= len(products):
                        selected_product = products[product_num - 1]
                        shopping_list.append((selected_product, quantity))
                    else:
                        print("Invalid product number. Please try again.")
                except ValueError:
                    print("Invalid input format. Please use 'product_number quantity'.")

            # Process the order
            try:
                total_price = store.order(shopping_list)
                print(f"\nOrder placed successfully! Total price: {total_price:.2f} dollars.")
            except Exception as e:
                print(f"Error while processing order: {e}")

        elif choice == "4":
            # Quit
            print("Thank you for shopping with us! Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    start(best_buy)
