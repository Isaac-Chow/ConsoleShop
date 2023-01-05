from user import User
from product import Product

class Buyer(User):
    def __init__(self, name, pw, email):
        super().__init__(name, pw, email)
        self.points=10

    def __str__(self):
        return f"Name: {self.name}\nPoints: {self.points}\nEmail: {self.email}"
    
    def add_to_cart(self, prod: Product):
        self.cart.appent(prod)
    def checkout(self):
        total_price=0
        print("===============================================")
        print("Isaac's everyting terminal store")
        print("-----------------------------------------------")
        print("Your items")
        print("-----------------------------------------------")
        for item in self.cart:
            print(f"Product ID: {item.id}\nName: {item.id}\nPrice: {item.price}")
        print("-----------------------------------------------")
        print(f"Total: {total_price}")
        print("Thanks for your purchase and visit! Come again!")
        print("===============================================")