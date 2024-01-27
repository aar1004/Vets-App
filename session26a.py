# Decorator
# rules:
# 1)create a function which takes function as input
# 2)create an inner function which should have same signature of target function
# 3)execute the passed function from inner function
# 4)return inner function from outer function
# 5)to decorate any sunction use @function


def compute_taxes(func):
    def inner(amount, taxes):
        if amount > 0 and amount <= 10000:
            taxes = 0.18
        elif amount > 10000:
            taxes = 0.25
        else:
            print("invalid amount")
        return func(amount, taxes)

    return inner


@compute_taxes
def pay(amount, taxes):
    return amount + (amount * taxes)


amount_to_pay = pay(50000, 0)
print("amount_to_pay:", amount_to_pay)
