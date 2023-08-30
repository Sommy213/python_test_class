import mysql.connector as sql

           

def main():
    db = Database()
    
    while True:
        print("\n1. Browse products")
        print("2. Add a product to cart")
        print("3.view the cart")
        print("4.place the order")
        print("5. view the order history")
        print("6.resigister new customer")
        print("7. update customer imformation")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            products = input('enter your produts:')
            category = input("Enter catory: ")
            stockquatity = input("Enter stock: ")
            
            User.register(db, category, stockquatity,products)
        elif choice == 2:
            cusomerid = input("Enter username: ")
            name= input("Enter name: ")
            email = input('enter your email:')
            shipping = ('enter your shipping address')
            
             
            user = User.login(db, cusomerid, email,shipping)
            if user:
                print(" successfully!")
            else:
                print("Invalid credentials!")
        elif choice == 3:
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            product = Product(db, name, price)
            product.add()
        elif choice == 4:
            products = Product.list_products(db)
            for product in products:
                print(f"ID: {product[0]}, Name: {product[1]}, Price: ${product[2]}")
        elif choice == 5:
            product_id = int(input("Enter product ID to add to cart: "))
            cart = Cart(db, user)
            cart.add_to_cart(product_id)
        elif choice == 6:
            cart = Cart(db, user)
            items = cart.list_cart()
            for item in items:
                print(f"Name: {item[0]}, Price: ${item[1]}")
        elif choice == 7:
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
        
        