class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name or price < 0 or quantity < 0:
            raise Exception("Sorry, Invalid Input")
            self.name = name
            self.price = price
            self.quantity = quantity
            self.active = True

    def set_quantity(self, quantity: int):
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def get_quantity(self) -> float:
        return self.quantity

    def is_active(self) -> bool:
        """Getter function for active."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self) -> str:
        """Returns a string that represents the product."""
        product_info = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        print(product_info)  # Print for demonstration
        return product_info

    def buy(self, quantity) -> float:
        """
                Buys a given quantity of the product.
                Returns the total price of the purchase.
                Updates the quantity of the product.
                Raises an exception in case of invalid quantity or insufficient stock.
                """
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than 0.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)  # Update quantity
        return total_price
