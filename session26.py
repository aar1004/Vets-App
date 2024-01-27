# def outer():
#     print("this is outer function")

#     def inner():
#         print("this is inner function")

#     inner()

# outer()


def outer():
    print("this is outer function")

    def inner():  # local function/nested function
        print("this is inner function")

    print("inner is", inner)
    # inner()
    return inner


result = outer()
print("outer is", outer)
result()
