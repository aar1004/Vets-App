from oops1 import Menu, Restaurant


def apply_promo_code(amount, promo_code):
    if promo_code == "WELCOME50":
        if amount >= 159:
            print("Promo Code Applied Successfully...")

            discount = 0.50 * amount

            if discount >= 100:
                discount = 100

            amount_to_pay = amount - discount
            print("Please Pay: \u20b9", amount_to_pay)
        else:
            print("Amount is Lesser for Promo Code...")
            print("Please Pay: \u20b9", amount)

    elif promo_code == "ZOMPAYTM":
        if amount >= 299:
            print("Promo Code Applied Successfully...")

            discount = 0.20 * amount

            if discount >= 50:
                discount = 50

            amount_to_pay = amount - discount
            print("Please Pay: \u20b9", amount_to_pay)
            print("You will get a cashback of: \u20b9 25")
        else:
            print("Amount is Lesser for Promo Code...")
            print("Please Pay: \u20b9", amount)
    else:
        print("Promo Code Invalid")
        print("Please Pay: \u20b9", amount)


class my_dictionary(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value


def main():
    menu = [
        Menu("dal", 300),
        Menu("parantha", 40),
        Menu("noodles", 150),
        Menu("burger", 200),
        Menu("fries", 90),
        Menu("cola", 50),
    ]

    restaurant = [Restaurant("AMRIK SUKHDEV", menu), Restaurant("RAJA DHABA", None)]

    for idx in range(len(restaurant)):
        restaurant[idx].show()

    print()
    option_restaurant = int(input("enter the number(1-2):"))
    if option_restaurant == 1:
        for i in range(len(menu)):
            menu[i].show()

    item_names = []
    quantities = []
    food_cart = []  # price

    while True:
        item_name = input("Enter Dish Name to add in Cart: ")
        quantity = input("Enter Dish Quantity: ")
        dict_obj = my_dictionary()
        dict_obj.add(item_name, quantity)
        item_names.append(item_name)
        quantities.append(quantity)
        for idx in range(len(menu)):
            if menu[idx].name == item_name:
                price = menu[idx].amount * int(quantity)
        food_cart.append(price)

        choice = input("Do You wish to add more items? (yes/no)")
        if choice == "no":
            break

    print(item_names)
    print(quantities)
    print(food_cart)

    amount = sum(food_cart)
    print("TOTAL AMOUNT: \u20b9", amount)

    promo_code = input("Enter Promo Code: ")
    apply_promo_code(amount, promo_code)


if __name__ == "__main__":
    main()
