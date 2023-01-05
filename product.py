class Product:
    def __init__(self, id, name, description, price, category):
        self.name=name
        self.description=description
        self.price=price
        self.category=category
        self.id=id

    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}\nID: {self.id}"

    def details(self):
        return f"\tName: {self.name}\t\nDescription: {self.description}\t\nPrice: {self.price}\t\nCategory: {self.category}\t\nID: {self.id}"


