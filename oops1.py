class Menu:
    def __init__(self, name="", amount=0):
        self.name = name
        self.amount = amount

    def show(self):
        print(self.name, "|", self.amount)


class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu

    def show(self):
        print(self.name)
