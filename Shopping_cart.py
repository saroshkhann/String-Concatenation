class Cart:
    def __init__(self):
        self.products = [
            {"name": "Laptop", "price": 100000, "stock": 5},
            {"name": "Phone", "price": 50000, "stock": 3},
            {"name": "Headphones", "price": 3000, "stock": 1}
        ]
        self.cart = []
        self.orders = []
        self.balance = 500000

    def menu(self):
        print("\n")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Remove from Cart")
        print("5. Checkout")
        print("6. Exit")

    def view_products(self):
        print("Available Products: ")
        counter = 1

        for product in self.products:
            print(f"{counter}. {product['name']} - {product['price']} PKR - Stock: {product['stock']}")
            counter+=1

    def add_to_cart(self):
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity"))
        if quantity <= 0:
            print("Enter valid quantity!")
            return

        found = False
        for product in self.products:
            if product["name"].lower() == name.lower():
                found= True
                if product["stock"] >= quantity:
                    product["stock"] -= quantity

                if product["stock"] < quantity:
                    print("Not enough stock available!")
                    return

                for item in self.cart:
                    if item["name"].lower() == name.lower():
                        item["quantity"] += quantity
                        print("Updated quantity in cart!")
                        return

                self.cart.append({"name": product['name'], "price": product['price'], "quantity": quantity})
                print("Added to cart successfully!")
                return
        if not found:
            print("Product not found!")


    def view_cart(self):
        if len(self.cart) == 0:
            print("Your cart is empty!")
            return

        print("Your Cart: ")
        total = 0

        for item in self.cart:
            item_total = item["price"] * item["quantity"]
            total += item_total
            print(f"{item['name']} - {item['quantity']} x {item['price']} = {item_total}")

        print(f"\nTotal: {total} PKR")

    def remove_from_cart(self):
        remove_product  = input("Enter product name to remove: ")
        found = False

        for product in self.products:
            for item in self.cart:
                if item['name'].lower() == remove_product.lower():
                    if product["name"].lower() == item["name"].lower():
                        product["stock"] += item["quantity"]
                    self.cart.remove(item)
                    print("Removed successfully!")

                    found = True
            if not found:
                print("Item not found in cart!")

    def checkout(self):
        if len(self.cart) == 0:
            print("Your cart is empty!")
            return
        total = 0
        print("You Cart: ")

        for item in self.cart:
            item_total = item["price"] * item["quantity"]
            total+= item_total
            print(f"{item['name']} - {item['quantity']} x {item['price']} = {item_total}")

        if total <= self.balance:
            if total > 20000:
                print("\nYou get a discount of 10%")
                discount = total * 0.1
                print(f"\nTotal Bill: {total - discount} PKR")
            else:
                print(f"\nTotal Bill: {total} PKR")

            print("Thank you for shopping! ")
            self.balance -= total
            print(f"Remaining Balance: {self.balance + discount} PKR")
            self.cart.clear()
        else:
            print("Insufficient money")


user = Cart()

is_on = True

while is_on:
    user.menu()
    choice = int(input("Please enter your choice: "))
    print("\n" * 20)
    if choice == 1:
        user.view_products()
    elif choice == 2:
        user.add_to_cart()
    elif choice == 3:
        user.view_cart()
    elif choice == 4:
        user.remove_from_cart()
    elif choice == 5:
        user.checkout()
    else:
        is_on = False