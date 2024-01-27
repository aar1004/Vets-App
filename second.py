class Recharge:
    def __init__(self, phone_number="", operator="airtel", amount=0):
        self.phone_number = phone_number
        self.operator = operator
        self.amount = amount

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("phone number is", self.phone_number)
        print("operator is", self.operator)
        print("phone number is", self.amount)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")


recharge1 = Recharge("+91 51764567890", "bsnl", 670)
recharge2 = Recharge("+91 51764567780", "jio", 780)
recharge3 = Recharge("+91 51764545690", "airtel", 1000)

recharge1.show()
recharge2.show()
recharge3.show()
