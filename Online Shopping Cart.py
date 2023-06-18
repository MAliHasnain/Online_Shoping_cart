from abc import ABCMeta, abstractmethod
from datetime import datetime, date, timedelta


class User(metaclass=ABCMeta):

    # This is an abstract method, which is over-ridden by the Admin and Customer classes
    @abstractmethod
    def Login(self):
        pass


class Products:
    lst = []

    # In this Method, We are printing all the products on screen for any user to view. If the User is the admin, the items in stock are also printed,
    # whereas for the customer, this quantity is shown for only the products with 10 or lesser than 10 items in stock
    def view_items(self, k = 0):
        if k == 1:
            with open("products.txt", "r") as f:
                self.lst = eval(f.read())
                if self.lst == []:
                    print("The Products list is empty at the moment\n")
                else:
                    print("\t\t\t\t\t\t\t\t\t PRODUCTS LIST\n")
                    print("------------------------------------------------------------------------------------------------------")
                    print(f'{"S.No:":12s}{"Product Name:":20s}{"Price:":20s}')
                    print("------------------------------------------------------------------------------------------------------")
                    for i in range(len(self.lst)):
                        print(f'{f"{(i + 1)}:":12s}{f"{self.lst[i][0]}":20s}{f"{self.lst[i][1]} PKR":20s}', end = "")
                        if self.lst[i][2] == "0":
                            print("Out of Stock!!!")
                        elif int(self.lst[i][2]) <= 10:
                            print(f"Only {self.lst[i][2]} items remaining!!!")
                        else:
                            print()
                    print("------------------------------------------------------------------------------------------------------\n")
        else:
            with open("products.txt", "r") as f:
                print("\t\t\t\t\t\t\t\t PRODUCTS LIST\n")
                self.lst = eval(f.read())
                if self.lst == []:
                    print("The Products list is empty at the moment\n")
                else:
                    print("------------------------------------------------------------------------------------------")
                    print(f'{"S.No:":12s}{"Product Name:":20s}{"Price:":20s}{"Quantity"}')
                    print("------------------------------------------------------------------------------------------")
                    for i in range(len(self.lst)):
                        print(f'{f"{(i + 1)}:":12s}{f"{self.lst[i][0]}":20s}{f"{self.lst[i][1]} PKR":20s}{self.lst[i][2]}')
                    print("------------------------------------------------------------------------------------------\n")

    # This method is only accessible to the Admin, who can add items to the main Product list using this function
    def add_items(self):
        self.view_items()
        with open("products.txt", "a+") as f:
            f.seek(0)
            self.lst = eval(f.read())
            while True:
                k = 0
                Name = input("Please enter the name of the item: ")
                for i in self.lst:
                    if Name in i:
                        print("\nThis product is already present, please enter a new one\n")
                        k = 1
                        break
                if k == 0:
                    Price = input('Please enter the price of the item: ')
                    Stock = input("Please enter the quantity of the item in stock: ")
                    self.lst.append([Name, Price, Stock])
                    print("\n\t\t\t\tITEM ADDED SUCCESSFULLY")
                    a = input("\nDo you want to add another item, or go back to the MAIN MENU?\nPress Y to Add more items, and anything else to go back: ").upper()
                    print()
                    if a != "Y":
                      break
            f.truncate(0)
            f.write(str(self.lst))

    # This method is only accessible to the Admin, who can remove items from the main Product list using this function
    def remove_items(self):
        self.view_items()
        while True:
            with open("products.txt", "a+") as f:
                f.seek(0)
                self.lst = eval(f.read())
                try:
                    x = int(input("Please enter the serial number of the item which you want to remove: "))
                    if x <= 0:
                        raise Exception
                except ValueError as E:
                    print("\nThe current value you entered was not an integer. Please enter a integer value.\n")
                except Exception:
                    print("\nPlease enter a positive integer value\n ")
                else:
                    if x <= len(self.lst):
                        del self.lst[x - 1]
                        f.truncate(0)
                        f.write(str(self.lst))
                        print("\n\t\t\t\tITEM REMOVED SUCCESSFULLY")
                        a = input("\nDo you want to remove another item, or go back to the MAIN MENU?\nPress Y to Remove more items, and anything else to go back: ").upper()
                        print()
                        if a != "Y":
                            break
                    else:
                        print("\nThe item does not exist\n")

    # This method is only accessible to the Admin, who can replace items in the main Product list using this function
    def replace_items(self):
        self.view_items()
        while True:
            with open("products.txt", "a+") as f:
                f.seek(0)
                self.lst = eval(f.read())
                try:
                    x = int(input("Please enter the serial number of the item which you want to replace: "))
                    if x <= 0:
                        raise Exception
                except ValueError as E:
                    print("\nThe current value you entered was not an integer. Please enter a integer value.\n")
                except Exception:
                    print("\nPlease enter a positive integer value\n ")
                else:
                    if x <= len(self.lst):
                        Name = input("Please enter the name of the item: ")
                        Price = input('Please enter the price of the item: ')
                        Stock = input("Please enter the quantity of the item in stock: ")
                        self.lst[x-1] = [Name, Price, Stock]
                        f.truncate(0)
                        f.write(str(self.lst))
                        print("\n\t\t\t\tITEM REPLACED SUCCESSFULLY")
                        a = input("\nDo you want to replace another item?\nPress Y to Replace more items, and anything else to go back:").upper()
                        print()
                        if a != "Y":
                            break
                    else:
                        print("\nThe item does not exist\n")

    # This method is only accessible to the Admin, who can change the price of items in the main Product list using this function
    def change_price(self):
        self.view_items()
        while True:
            with open("products.txt", "a+") as f:
                f.seek(0)
                self.lst = eval(f.read())
                try:
                    x = int(input("Please enter the Serial Number of the item whose price you want to change: "))
                    if x <= 0:
                        raise Exception
                except ValueError as E:
                    print("\nThe current value you entered was not an integer. Please enter a integer value.\n")
                except Exception:
                    print("\nPlease enter a positive integer value\n ")
                else:
                    if x <= len(self.lst):
                        Price = input("Please enter the New Price of said Item: ")
                        self.lst[x-1][1] = Price
                        f.truncate(0)
                        f.write(str(self.lst))
                        print("\n\t\t\t\tPRICE UPDATED SUCCESSFULLY")
                        a = input("\nDo you want to Change the Price of another item, or go back to the MAIN MENU?\nPress Y to Change more Prices, and anything else to go back:").upper()
                        print()
                        if a != "Y":
                            break
                    else:
                        print("\nThe item does not exist\n")

    # This method is only accessible to the Admin, who can add stock of items present in the main Product list using this function
    def Add_Stock(self):
        self.view_items()
        while True:
            with open("products.txt", "a+") as f:
                f.seek(0)
                self.lst = eval(f.read())
                try:
                    x = int(input("Please enter the name of the item whose stock you want to increase: "))
                    if x <= 0:
                        raise Exception
                except ValueError as E:
                    print("\nThe current value you entered was not an integer. Please enter a integer value.\n")
                except Exception:
                    print("\nPlease enter a positive integer value\n ")
                else:
                    if x <= len(self.lst):
                        while True:
                            try:
                                Stock = int(input("Please enter the quantity of incoming stock: "))
                            except ValueError as E:
                                print("\nThe current value you entered was not an integer. Please enter a integer value.\n")
                            else:
                                y = int(self.lst[x - 1][2])
                                y += Stock
                                self.lst[x-1][2] = str(y)
                                f.truncate(0)
                                f.write(str(self.lst))
                                print("\n\t\t\t\tSTOCK ADDED SUCCESSFULLY")
                                break
                        a = input("\nDo you want to increase the stock of another item, or go back to the MAIN MENU?\nPress Y to Add more stock, and anything else to go back: ").upper()
                        print()
                        if a != "Y":
                            break
                    else:
                        print("\nThe item does not exist\n")

    # This method is only accessible to the Admin, who can delete all the items in the main Product list using this function
    def erase_all(self):
        with open("products.txt", "a+") as f:
            f.seek(0)
            f. truncate(0)
            f.write("[]")
            print("\n\t\t\t\t\tERASED ALL PRODUCTS SUCCESSFULLY\n")


class Admin(User):

    # This method is only accessible to the Admin, who can change his own login details using this method
    def Change_Credentials(self):
        with open("password.txt", "a+") as f:
            f.seek(0)
            while True:
                try:
                    x = int(input("What do you want to change \n1: The ID \n2: The Password \n3: Both the ID and Password \n4: Go back\nEnter your choice: "))
                    print()
                except ValueError as E:
                    print("\nThe current value you entered was not an integer. Please enter a integer value.\n")
                else:
                    if x == 1:
                        self.lst = eval(f.read())
                        ID = input("Please enter the new ID: ")
                        self.lst[0] = ID
                        f.truncate(0)
                        f.write(str(self.lst))
                        print("\n\t\tAdmin ID Changed Successfully")
                        break
                    elif x == 2:
                        self.lst = eval(f.read())
                        Pass = input("Please enter the new Pass: ")
                        self.lst[1] = Pass
                        f.truncate(0)
                        f.write(str(self.lst))
                        print("\n\t\tAdmin Password Changed Successfully")
                        break
                    elif x == 3:
                        ID = input("Please enter the new ID: ")
                        Pass = input("Please enter the new Password: ")
                        f.truncate(0)
                        f.write(str([ID, Pass]))
                        print("\n\t\tAdmin ID and Password Changed Successfully")
                        break
                    elif x == 4:
                        break
                    else:
                        print("Please enter a valid input\n")

    # This Method is accessible by the Admin only, who can login using this function and then choose what to do
    def Login(self):
        A = Products()
        C = Order()
        count = 0
        while True:
            count += 1
            if count == 6:
                print("\t\tRedirecting to Startup Page due to multiple incorrect attempts\n")
                break
            self.ID = input('Enter your ID: ')
            self.Pass = input('Enter your password: ')
            print()
            f = open('password.txt')
            k = eval(f.read())
            a = "Y"
            if self.ID == k[0]:
                while True:
                    if self.Pass == k[1]:
                        try:
                            print("-----------------------------------------------------------------------------------------")
                            print("\t\t\t\t\t\t\t\t\tMAIN MENU")
                            print("-----------------------------------------------------------------------------------------\n")
                            x = int(input("Please choose what do you want to do: \n1: View Items \n2: Add Items \n3: Remove Items \n4: Edit Items \n5: Erase All \n6: Check a Customers Current Order \n7: Check a Customers Order History\n8: Logout \n0: Change Credentials\nEnter Your Choice: "))
                            print()
                        except ValueError as E:
                            print("\nThe current value you entered was not an integer. Please enter a integer value.\n")
                        else:
                            while True:
                                if x == 1:
                                    A.view_items()
                                elif x == 2:
                                    A.add_items()
                                elif x == 3:
                                    A.remove_items()
                                elif x == 4:
                                    while True:
                                        try:
                                            y = int(input("Do you want to : \n1: Replace Items \n2: Change Price \n3: Add Stock \n4: Go back \nEnter your choice: "))
                                            if y <= 0 or y >= 5:
                                                raise Exception
                                        except ValueError as E:
                                            print("\nThe current value you entered was not an integer. Please enter a integer value.\n")
                                        except Exception:
                                            print("\nPlease give a correct input\n")
                                        else:
                                            if y == 1:
                                                A.replace_items()
                                            elif y == 2:
                                                A.change_price()
                                            elif y == 3:
                                                A.Add_Stock()
                                            else:
                                                print()
                                                pass
                                            break
                                elif x == 5:
                                    A.erase_all()
                                elif x == 6:
                                    while True:
                                        self.UserID = input("Please enter the UserID of the Customer: ")
                                        print()
                                        with open("Customers\\Customers.txt", "r") as f:
                                            f.seek(0)
                                            l = 0
                                            self.lst = eval(f.read())
                                            for i in self.lst:
                                                if self.UserID == i[1]:
                                                    l = 1
                                                    C.check_order(self.UserID)
                                                    print()
                                                    break
                                            if l == 0:
                                                print("Please enter a correct UserID\n")
                                            else:
                                                break
                                elif x == 7:
                                    while True:
                                        self.UserID = input("Please enter the UserID of the Customer: ")
                                        print()
                                        with open("Customers\\Customers.txt", "r") as f:
                                            f.seek(0)
                                            l = 0
                                            self.lst = eval(f.read())
                                            for i in self.lst:
                                                if self.UserID == i[1]:
                                                    l = 1
                                                    C.order_history(self.UserID)
                                                    break
                                            if l == 0:
                                                print("Please enter a correct UserID\n")
                                            else:
                                                break
                                elif x == 8:
                                    a = "N"
                                    break
                                elif x == 0:
                                    self.Change_Credentials()
                                else:
                                    print("Please enter a valid response")
                                    break
                                a = input("Do you want to do anything else? Press Y to continue, and anything else to exit: ").upper()
                                print()
                                break

                    else:
                        print("Please enter a correct password\n")
                        break
                    if a != "Y":
                        break

            else:
                print("Please enter a correct ID\n")
            if a != "Y":
                break


class Customer(User):

    # This Method is accessible only by User who is a prospective Customer, who signs up using this method
    def New_Customer(self):
        self.Name = input("Please enter your name: ")
        with open("Customers\\Customers.txt", "a+") as f:
            f.seek(0)
            self.lst = eval(f.read())
            flag = 0
            while flag == 0:
                self.UserID = input("Please enter a Unique Username: ")
                self.Password = input("Please enter a Password: ")
                k = 0
                for i in self.lst:
                    if self.UserID == i[1]:
                        k = 1
                        break
                if k == 1:
                    print("\nThis username is already taken. Please enter another one.\n")
                else:
                    self.Email = input("Please enter your Email Address: ")
                    self.Number = input("Please enter you Phone Number: ")
                    self.Address = input("Please enter your Address: ")
                    L = []
                    L.extend([self.Name, self.UserID, self.Password, self.Email, self.Number, self.Address])
                    self.lst.append(L)
                    print("\nNew ID created Succesfully\n")
                    f.truncate(0)
                    f.write(str(self.lst))
                    with open("Customers\\" + self.UserID + ".txt", "w") as g:
                        g.write(str([]))
                    with open("Customers\\" + self.UserID + " Order.txt", "w") as k:
                        k.write(self.UserID)
                    break
        self.Login()

    # This Method is only accessible to the Customer, who uses it to Login and then choose what to do
    def Login(self):
        A = Products()
        B = Cart()
        C = Order()
        count = 0
        print("\t\t\t\t\t\t CUSTOMER LOGIN\n")
        while True:
            count += 1
            if count == 6:
                print("\t\tRedirecting to Startup Page due to multiple incorrect attempts\n")
                break
            a = "Y"
            self.UserID = input("Please enter your UserID: ")
            self.Password = input("Please enter your password: ")
            print()
            self.File = self.UserID + ".txt"
            with open("Customers\\Customers.txt", "r") as g:
                k = eval(g.read())
                user = False
                for i in k:
                    if i[1] == self.UserID:
                        user = True
                        if i[2] == self.Password:
                            while True:
                                try:
                                    print("-----------------------------------------------------------------------------------------")
                                    print("\t\t\t\t\t\t\t\t\tMAIN MENU")
                                    print("-----------------------------------------------------------------------------------------\n")
                                    x = int(input("Do you want to: \n1: View Cart \n2: View Products \n3: Add Items to cart \n4: Edit Quantity \n5: Remove Items from cart \n6: Delete Cart \n7: Checkout\n8: Check Your Order\n9: Check Your History\n0: Log Out\nEnter your choice: "))
                                    print()
                                except ValueError as E:
                                    print("\nThe current value you entered was not an integer. Please enter a integer value.\n")
                                else:
                                    if x == 1:
                                        B.View_Cart(self.File)
                                    elif x == 2:
                                        A.view_items(1)
                                    elif x == 3:
                                        A.view_items(1)
                                        B.Add_to_cart(self.File)
                                    elif x == 4:
                                        B.Edit_Quantity(self.File)
                                    elif x == 5:
                                        B.Remove_from_Cart(self.File)
                                    elif x == 6:
                                        B.Delete_All(self.File)
                                    elif x == 7:
                                        B.Checkout(self.UserID)
                                        C.check_order(self.UserID)
                                    elif x == 8:
                                        C.check_order(self.UserID)
                                    elif x == 9:
                                        C.order_history(self.UserID)
                                    elif x == 0:
                                        a = "N"
                                        break
                                    else:
                                        print("Please enter a valid response\n")
                                        break
                                    a = (input("Do you want to do anything else? Press Y to continue, and anything else to exit: ")).upper()
                                    print()
                                    if a != "Y":
                                        break
                        else:
                            print("Please enter a correct password\n")
                            break
                        if a != "Y":
                            break
                if user == False:
                    print("Please enter a correct username\n")
            if a != "Y":
                break


class Cart:
    lst = []

    # This Method is only accessible by the Customer, who can view their cart using this method
    def View_Cart(self, UserID):
        with open("Customers\\" + UserID, "r") as f:
            f.seek(0)
            self.lst = eval(f.read())
            if self.lst == []:
                print("Your Cart is Empty at the moment\n")
                pass
            else:
                print(f"\t\t\t\t\t\t\t\t\t\t CUSTOMERS CART\n")
                total = 0
                L = []
                for i in self.lst:
                    a = (int(i[1]) * i[2])
                    total += a
                    L.append(a)
                print("------------------------------------------------------------------------------------------------------")
                print(f'{"S.No:":12s}{"Product Name:":20s}{"Price:":20s}{"Quantity:":20s}Total Cost:')
                print("------------------------------------------------------------------------------------------------------")
                for i in range(len(self.lst)):
                    print(f'{f"{(i + 1)}:":12s}{f"{self.lst[i][0]}":20s}{f"{self.lst[i][1]} PKR":20s}{f"{self.lst[i][2]}":20s}{f"{L[i]}":5s}PKR')
                print("------------------------------------------------------------------------------------------------------")
                print(f'{"The total bill is:":72s}{total} PKR\n')

    # This Method is only accessible to the Customer, who uses this Method to add products to their cart
    def Add_to_cart(self, UserID):
        print()
        self.View_Cart(UserID)
        with open("Customers\\" + UserID, "a+") as f:
            f.seek(0)
            self.lst = eval(f.read())
            with open("Products.txt", "r") as k:
                k.seek(0)
                products = eval(k.read())
                while True:
                    try:
                        x = int(input("Please enter the serial number of the item you want to add to cart: "))
                        y = int(input("Select Quantity: "))
                        if x <= 0 or y <= 0:
                            raise Exception
                    except ValueError as E:
                        print("\nThe current value you entered was not an integer. Please enter a integer value.\n")
                    except Exception:
                        print("\nPlease enter a positive integer\n")
                    else:
                        if x <= len(products):
                            h = products[(x - 1)]
                            k = 0
                            for i in self.lst:
                                if h[0] == i[0]:
                                    Quantity = i[2]
                                    Quantity += y
                                    i[2] = Quantity
                                    k = 1
                                    print("\n\tTHE QUANTITY OF THE ITEM IN CART HAS BEEN UPDATED SUCCESSFULLY")
                                    break
                            if k == 0:
                                add = [h[0], h[1], y]
                                self.lst.append(add)
                                print("\n\t\tITEM ADDED TO CART SUCCESSFULLY")
                            y = input("\nDo you want add more items, or go back to the Main Menu?\nEnter Y to Add more items, and anything else to go back: ").upper()
                            print()
                            if y != "Y":
                                break
                        else:
                            print("\nThe item does not exist\n")
            f.truncate(0)
            f.write(str(self.lst))

    # This Method is only accessible to the Customer, who uses this Method to edit the quantity of the products present in their cart
    def Edit_Quantity(self, UserID):
        self.View_Cart(UserID)
        while True:
            with open("Customers\\" + UserID, "a+") as f:
                f.seek(0)
                self.lst = eval(f.read())
                try:
                    x = int(input("Please enter the serial number of the item whose quantity you want to change: "))
                    if x <= 0:
                        raise Exception
                except ValueError as E:
                    print("\nThe current value you entered was not an integer. Please enter a integer value.\n")
                except Exception:
                    print("\nPlease enter a positive integer value\n ")
                else:
                    if x <= len(self.lst):
                        try:
                            y = int(input("Please enter the new quantity: "))
                        except ValueError as E:
                            print("\nThe current value you entered was not an integer. Please enter a integer value.\n")
                        else:
                            if y == 0:
                                del self.lst[x - 1]
                                f.truncate(0)
                                f.write(str(self.lst))
                                print("\n\t\tITEM REMOVED FROM CART SUCCESSFULLY")
                            else:
                                self.lst[x - 1][2] = y
                                f.truncate(0)
                                f.write(str(self.lst))
                                print("\n\tQUANTITY OF THE ITEM IN CART HAS BEEN UPDATED SUCCESSFULLY")
                            a = input("\nDo you want to change the quantity of another item, or go back to the MAIN MENU?\nPress Y to Edit more items, and anything else to go back: ").upper()
                            print()
                            if a != "Y":
                                break
                    else:
                        print("\nThe item does not exist\n")

    # This Method is only accessible to the Customer, who uses this Method to remove products from their cart
    def Remove_from_Cart(self, UserID):
        self.View_Cart(UserID)
        while True:
            with open("Customers\\" + UserID, "a+") as f:
                f.seek(0)
                self.lst = eval(f.read())
                try:
                    x = int(input("Please enter the serial number of the item which you want to remove: "))
                    if x <= 0:
                        raise Exception
                except ValueError as E:
                    print("\nThe current value you entered was not an integer. Please enter a integer value.\n")
                except Exception:
                    print("\nPlease enter a positive integer value\n ")
                else:
                    if x <= len(self.lst):
                        del self.lst[x - 1]
                        f.truncate(0)
                        f.write(str(self.lst))
                        print("\n\t\tITEM REMOVED FROM THE CART SUCCESSFULLY")
                        a = input("\nDo you want to remove another item, or go back to the MAIN MENU?\nPress Y to Remove more items, and anything else to go back: ").upper()
                        print()
                        if a != "Y":
                            break
                    else:
                        print("\nThe item does not exist\n")

    # This Method is only accessible to the Customer, who uses this Method to completely erase their cart
    def Delete_All(self, UserID):
        with open("Customers\\" + UserID, "a+") as f:
            f.seek(0)
            f.truncate(0)
            f.write("[]")
            print("\n\t\t\t\t\t\tCART EMPTIED SUCCESSFULLY\n")

    # This Method is only accessible to the Customer, who uses this Method to checkout and empty their cart and write the Order and History files
    def Checkout(self, UserID):
        with open("Customers\\" + UserID + ".txt", "a+") as f:
            f.seek(0)
            self.lst = eval(f.read())

            if self.lst == []:
                print("Please Add some items to cart before you checkout\n")
                return

        with open("Customers\\" + UserID + ".txt", "a+") as f:
            f.seek(0)
            self.lst = eval(f.read())
            total = 0
            L = []

            y = input("Are you sure you want to check out? \nPress Y to continue, and anything else to go back: ").upper()
            print()
            if y == "Y":
                while True:
                    File = UserID + ".txt"
                    try:
                        choice = int(input("Do you want to add or remove any item(s)?\nPress 1 to Add, 2 to remove, and 3 to proceed: "))
                        print()
                    except ValueError as E:
                        print("\nThe current value you entered was not an integer. Please enter a integer value.\n")
                    else:
                        if choice == 1:
                            self.Add_to_cart(File)
                        elif choice == 2:
                            self.Remove_from_Cart(File)
                        elif choice == 3:
                            break
                        else:
                            print("\nPlease enter a valid choice\n")

                with open("products.txt", "a+") as p:
                    p.seek(0)
                    lst_new = eval(p.read())
                    count1 = -1
                    for i in self.lst:
                        count1 += 1
                        count2 = -1
                        for j in lst_new:
                            count2 += 1
                            if i[0] == j[0]:
                                if int(i[2]) <= int(j[2]):
                                    cost = (int(i[1]) * i[2])
                                    total += cost
                                    L.append(cost)
                                    value = int(lst_new[count2][2]) - int(i[2])
                                    lst_new[count2][2] = str(value)
                                elif int(j[2]) != 0:
                                    while True:
                                        try:
                                            x = int(input(f"The current stock is lesser than the quantity you require. Do you want to: \n1: Buy {j[2]} items, and get the rest as soon as the stock arrives\n2: Buy {j[2]} items only \n3: Buy no items\nEnter your choice: "))
                                            print()
                                            if x < 1 or x > 3:
                                                raise Exception
                                        except ValueError as E:
                                            print("\nThe current value you entered was not an integer. Please enter a integer value.\n")
                                        except Exception:
                                            print("\nPlease enter a valid value\n")
                                        else:
                                            if x == 1:
                                                cost = (int(i[1]) * i[2])
                                                total += cost
                                                L.append(cost)
                                                lst_new[count2][2] = "0"
                                                break
                                            elif x == 2:
                                                cost = (int(i[1]) * int(j[2]))
                                                total += cost
                                                L.append(cost)
                                                lst_new[count2][2] = "0"
                                                break
                                            else:
                                                del self.lst[count1]
                                                break
                                else:
                                    print("\nThe Stock for this item has ended. It is being removed from your cart. Sorry for any inconvenience.\n")
                                    del self.lst[count1]
                    p.truncate(0)
                    p.write(str(lst_new))


            while True:
                x = input("What type of shipping do you want? \n1: Delivery Today (Costs 300 PKR) \n2: 1 Day Rush (Delivery within 1 working day, costs 200 PKR) \n3: Normal (Delivery in 2 working days, cost 100 PKR)\nEnter your choice: ")
                if x == "1":
                    Fee = 300
                    total += Fee
                    break
                elif x == "2":
                    Fee = 200
                    total += Fee
                    break
                elif x == "3":
                    Fee = 100
                    total += Fee
                    break
                else:
                    print("\nPlease give a valid input\n")

            with open("Customers\\" + UserID + " Order.txt", "w") as k:
                k.truncate(0)
                k.write(f'{"Report Generated on:":40s}')
                k.write(str(datetime.now()))
                k.write("\n\n")
                with open("Customers\\Customers.txt", "r") as q:
                    Data = eval(q.read())
                for i in Data:
                    if UserID == i[1]:
                        customer = i
                        break
                k.write(f'{"Name:":40s}')
                k.write(customer[0])
                k.write("\n")
                k.write(f'{"Email Address:":40s}')
                k.write(customer[3])
                k.write("\n")
                k.write(f'{"Contact Number:":40s}')
                k.write(customer[4])
                k.write("\n")
                k.write(f'{"Address:":40s}')
                k.write(customer[5])
                k.write("\n\n")
                if x == "1":
                    k.write(f'{"Your item(s) will be delivered on:":40s}{str(date.today())}\n')
                elif x == "2":
                    k.write(f'{"Your item(s) will be delivered on:":40s}{str(date.today() + timedelta(days = 1))}\n')
                else:
                    k.write(f'{"Your item(s) will be delivered on:":40s}{str(date.today() + timedelta(days = 2))}\n')
                k.write("\n")
                k.write("------------------------------------------------------------------------------------------------------\n")
                k.write(f'{"S.No:":12s}{"Product Name:":20s}{"Price:":20s}{"Quantity:":20s}Total Cost:\n')
                k.write("------------------------------------------------------------------------------------------------------\n")
                for i in range(len(self.lst)):
                    k.write(f'{f"{(i + 1)}:":12s}{f"{self.lst[i][0]}":20s}{f"{self.lst[i][1]} PKR":20s}{f"{self.lst[i][2]}":20s}{f"{L[i]}":5s}PKR')
                    k.write("\n")
                k.write(f'{"The Delivery Fee is:":72s}{f"{Fee}":5s}PKR \n')
                k.write("------------------------------------------------------------------------------------------------------\n")
                k.write(f'{"The total bill is:":72s}{total} PKR\n')
                if total >= 2500 and total <= 5000:
                    discount = round(0.95 * total, 9)
                elif total > 5000 and total <= 10000:
                    discount = round(0.925 * total, 9)
                elif total > 10000:
                    discount = round(0.9 * total, 9)
                if total >= 2500 and total <= 5000:
                    k.write(f'{"Congratulation!!!!!! You have recieved a discount of:":72s}5%\n')
                    k.write(f'{"The Discounted Total bill is:":72s}{discount} PKR')
                elif total > 5000 and total <= 10000:
                    k.write(f'{"Congratulation!!!!!! You have recieved a discount of:":72s}7.5%')
                    k.write(f'{"The Discounted Total bill is:":72s}{discount} PKR')
                elif total > 10000:
                    k.write(f'{"Congratulation!!!!!! You have recieved a discount of:":72s}10%')
                    k.write(f'{"The Discounted Total bill is:":72s}{discount} PKR')

            with open("Customers\\" + UserID + " History.txt", "a+") as g:
                g.read()
                g.write(f'{"Report Generated on:":40s}')
                g.write(str(datetime.now()))
                g.write("\n\n")
                g.write(f'{"Name:":40s}')
                g.write(customer[0])
                g.write("\n")
                g.write(f'{"Email Address:":40s}')
                g.write(customer[3])
                g.write("\n")
                g.write(f'{"Contact Number:":40s}')
                g.write(customer[4])
                g.write("\n")
                g.write(f'{"Address:":40s}')
                g.write(customer[5])
                g.write("\n\n")
                if x == "1":
                    g.write(f'{"Your item(s) will be delivered on:":40s}{str(date.today())}\n')
                elif x == "2":
                    g.write(f'{"Your item(s) will be delivered on:":40s}{str(date.today() + timedelta(days=1))}\n')
                else:
                    g.write(f'{"Your item(s) will be delivered on:":40s}{str(date.today() + timedelta(days=2))}\n')
                g.write("\n")
                g.write("------------------------------------------------------------------------------------------------------\n")
                g.write(f'{"S.No:":12s}{"Product Name:":20s}{"Price:":20s}{"Quantity:":20s}Total Cost:\n')
                g.write("------------------------------------------------------------------------------------------------------\n")
                for i in range(len(self.lst)):
                    g.write(f'{f"{(i + 1)}:":12s}{f"{self.lst[i][0]}":20s}{f"{self.lst[i][1]}":20s}{f"{self.lst[i][2]}":20s}{f"{L[i]}":5s}PKR')
                    g.write("\n")
                g.write(f'{"The Delivery Fee is:":72s}{f"{Fee}":5s}PKR \n')
                g.write("------------------------------------------------------------------------------------------------------\n")
                g.write(f'{"The total bill is:":72s}{total} PKR\n')
                if total >= 2500 and total <= 5000:
                    discount = round(0.95 * total, 9)
                elif total > 5000 and total <= 10000:
                    discount = round(0.925 * total, 9)
                elif total > 10000:
                    discount = round(0.9 * total, 9)
                if total >= 2500 and total <= 5000:
                    g.write(f'{"Congratulation!!!!!! You have recieved a discount of:":72s}5%\n')
                    g.write(f'{"The Discounted Total bill is:":72s}{discount} PKR')
                elif total > 5000 and total <= 10000:
                    g.write(f'{"Congratulation!!!!!! You have recieved a discount of:":72s}7.5%\n')
                    g.write(f'{"The Discounted Total bill is:":72s}{discount} PKR')
                elif total > 10000:
                    g.write(f'{"Congratulation!!!!!! You have recieved a discount of:":72s}10%\n')
                    g.write(f'{"The Discounted Total bill is:":72s}{discount} PKR')
                g.write("\n\n\n\n")
            f.truncate(0)
            f.write("[]")
            print()


class Order:

    # This Method is accessible to both the Admin and The Customer. The Customer uses it to check their own current Order only, while the Admin uses
    # it to check the current Order of any Customer, whose UserID they provide
    def check_order(self, UserID):
        with open("Customers\\" + UserID + " Order.txt", "r") as f:
            k = f.read()
            if k == UserID:
                print("Please place an order to view it!!!!\n")
            else:
                print(k)
                print()

    # This Method is accessible to both the Admin and The Customer. The Customer uses it to check their own history only, while the Admin uses it to
    # check the history of any Customer, whose UserID they provide
    def order_history(self, UserID):
        with open("Customers\\" + UserID + " Order.txt", "r") as g:
            k = g.read()
            if k == UserID:
                print("Please place an order to view your history!!!!\n")
            else:
                with open("Customers\\" + UserID + " History.txt", "r") as f:
                    print(f.read())
                    print()


# Main Driver Code, which asks the User whether they want to proceed as Customer or Admin
while True:
    try:
        x = int(input("Who do you want to proceed as?\n1: Administrator \n2: Customer \nEnter Your Choice: "))
        print()
    except ValueError as E:
        print("\nThe current value you entered was not an integer. Please enter a integer value.\n")
    else:
        if x == 1:
            print("\t\t\t\t\t\t ADMIN LOGIN\n")
            A = Admin()
            A.Login()
        elif x == 2:
            B = Customer()
            while True:
                try:
                    y = int(input("What do you want to do\n1: Login \n2: Sign Up \nEnter Your Choice: "))
                except ValueError as E:
                    print("\nThe current value you entered was not an integer. Please enter a integer value.\n")
                else:
                    if y == 1:
                        print()
                        B.Login()
                        break
                    elif y == 2:
                        print()
                        print("\t\t\t\t\t\t CUSTOMER SIGNUP\n")
                        B.New_Customer()
                        break
                    else:
                        print("\nPlease enter a valid response\n")
        else:
            print("\nPlease enter a valid response\n")

        a = input("If you wish to restart then enter Y, else enter anything else: ").upper()
        if a != "Y":
            break
        else:
            print()