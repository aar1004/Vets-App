import datetime


class Customer:
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.email = ""
        self.age = 0
        self.gender = ""
        self.address = ""
        self.createdon = ""

    def read_customer_data(self):
        self.name = input("enter customer name:")
        self.phone = input("enter customer phone number:")
        self.email = input("enter customer email:")
        self.age = input("enter customer age:")
        self.gender = input("enter customer gender:").lower()
        self.address = input("enter customer address:")
        self.createdon = datetime.datetime.today()
