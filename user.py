from random import randint
class User:
    # Parameters => Different for every user
    def __init__(self,name,pw,email):
        # Attributes 
        self.status=False
        
        self.id = f"{randint(1000,9999)}-{randint(1000,9999)}-{randint(1000,9999)}-{randint(1000,9999)}"
        self.name=name
        self.pw=pw
        self.email=email

    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}"

    def login(self):
        if not self.status:
            self.status=True

    def logout(self):
        if self.status:
            self.status=False

    def details(self):
        return f"Name: {self.name}\nEmail: {self.email}\nStatus: {self.status}"