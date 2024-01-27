def upgrade_to_meal(func):
    def inner(amount, taxes, meal_plan):
        if meal_plan == 1:
            print("upgrading to medium meal...")
            print("+ added coke")
            print("+ added fries")
            amount += 100
            taxes = 0.10
        elif meal_plan == 2:
            print("upgrading to large meal...")
            print("+ added large coke")
            print("+ added large fries")
            print("+ added ice cream")
            amount += 200
            taxes = 0.20
        else:
            print("thank for your purchase...")

        return func(amount, taxes, meal_plan)

    return inner


@upgrade_to_meal
def buy_burger(amount, taxes, meal_plan=0):
    return amount + (amount * taxes)


amount_to_pay = buy_burger(100, 0.10, 2)
print("amount_to_pay:", amount_to_pay)
