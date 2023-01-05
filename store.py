import os
from buyer import Buyer
from admin import Admin
import time
from product import Product

test_mode = "true"
# test_mode = "false"

my_buyer =Buyer("Billy", "billypw", "billy@billymicah.com")
buyer_2 =Buyer("Betty", "bettypw", "betty@bettymyer.com")
buyer_3 =Buyer("Mike", "mikepw", "mike@billymicah.com")

my_admin=Admin("Isaac", "isaacpw", "isaachychow@gmail.com")

buyer_list=[ my_buyer, buyer_2, buyer_3 ]
admin_list=[  ]

gamingpc=Product(1000,"Isaac's Product","Just a product",1500,"Gaming > Gear")
keyboard=Product(1001,"Isaac","Just a product",500,"Gaming > Gear")
mouse=Product(1002,"Isaac","Just a product",300,"Gaming > Gear")
minecraft=Product(1003,"Isaac","Just a product",2,"Gaming > Games")

my_products=[
    gamingpc, keyboard, mouse, minecraft
]

def homepage():
    print("===============================================")
    print("Welcome!")
    print("-----------------------------------------------")

    for item in my_products:
        print(item.details())
    print("===============================================")


def admin_homepage():
    print("===============================================")
    print("Welcome back!")
    print("-----------------------------------------------")
    print()
    print("Your products:")
    for item in my_products:
        print(item.details())
        print()

    print("===============================================")
    print("Your customers:")
    for user in buyer_list:
        print(user.details())
        print("-----------------------------------------------")
    print("===============================================")


def self_des():
    if test_mode == "false":
        print("Self destruction activated!")
        print("Activating in 3")
        time.sleep(1)
        print("Activating in 2")
        time.sleep(1)
        print("Activating in 1")
        time.sleep(1)
        os.sys("exit()")
    else:
        print("Testmode active, expect a self destruction if not active.")

def login():
    if len(buyer_list)>1:
        username=input("Please enter your name\n")
        username = username.strip()
        name_list=[ ]
        for item in buyer_list:
            name_list.append(item.name)

        name_list.append("Isaac")
        print(f"{name_list}")
        if (username not in name_list):
            print("You don't have an account!")
            time.sleep(1)
            self_des()
            login()

        elif (username in name_list):
            index_val = name_list.index(username)

            # User LogIn
            if username in name_list and username.lower() != "isaac":
                user_obj = buyer_list[index_val]
                password = input("Please enter you password\n")

                if password!=user_obj.pw:
                    print("Incorrect password!")
                    self_des()
                elif password==user_obj.pw:
                    homepage()

            # Admin Login
            if username.lower()=="isaac":
                password = input("Please enter you password\n")
                if password!=my_admin.pw:
                    print("Incorrect password!")
                    self_des()
                elif password==my_admin.pw:
                    admin_homepage()

def register():
    # Add 
    pass

def welcome():
    print("    >Login: [L]")
    print("    >Register: [R]")
    print("    >Exit")
    response = input("Please pick an option to proceed\n")

    # if response.lower() == "l":
        # login()
    # D - Don't 
    # R - Reapeat
    # Y - Yourself

    if response.lower() =="l" or response.lower() =="login":
        login()
    elif response.lower() =="r" or response.lower() =="register":
        register()
    elif response.lower() =="exit":
        # Use the exit function instead.
        exit()
    else:
        print("You entered something incorrectly!")
        self_des()

welcome()