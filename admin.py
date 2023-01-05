from user import User
from product import Product

class Admin(User):
    # Orders - List of orders
    # Catalogue - List of products
    def __init__(self,name,pw,email):
        
        super().__init__(name,pw,email)

        self.orders=[]
        self.catalog=[]

    def __str__(self):
        return f"name: {self.name}\nEmail: {self.email}"

    def add_products(self,prod: Product):
        if type(prod)!=Product.__name__():
            print("You can only pass pass products, please try again")
        self.catalog.append(prod)

    def remove_product(self,prod: Product):
        if type(prod)!=Product.__name__():
            print("You can only pass pass products, please try again")
        self.catalog.remove(prod)
    
    def sell_product(self,product):
        if product not in self.orders:
            print("Sorry buddy! That product has not been requested yet! [<-Not been ordered]")

    
    def track_catalog(self):
        categories=[]
        for i in range(len(self.catalog)):
            i.append(i.category)