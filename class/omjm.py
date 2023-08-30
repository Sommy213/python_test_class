class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"ID: {self.product_id} - {self.name} - ${self.price}"


class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product):
        self.items.append(product)

    def remove_from_cart(self, product_id):
        for product in self.items:
            if product.product_id == product_id:
                self.items.remove(product)
                break

    def calculate_total(self):
        return sum([product.price for product in self.items])

    def display_cart(self):
        for product in self.items:
            print(product)
        print(f"Total: ${self.calculate_total()}")


def main():
    # Sample products
    products = [
        Product(1, "T-shirt", 20),
        Product(2, "Jeans", 50),
        Product(3, "Shoes", 80)
    ]

    cart = Cart()

    while True:
        print("\nProducts available:")
        for product in products:
            print(product)

        print("\nOptions:")
        print("1. Add to cart")
        print("2. Remove from cart")
        print("3. View cart")
        print("4. Checkout and exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            product_id = int(input("Enter product ID to add: "))
            for product in products:
                if product.product_id == product_id:
                    cart.add_to_cart(product)
                    print(f"{product.name} added to cart!")
                    break

        elif choice == 2:
            cart.display_cart()
            product_id = int(input("Enter product ID to remove: "))
            cart.remove_from_cart(product_id)
            print(f"Product ID {product_id} removed!")

        elif choice == 3:
            cart.display_cart()

        elif choice == 4:
            cart.display_cart()
            print("Thank you for shopping!")
            break


if __name__ == "__main__":
    main()