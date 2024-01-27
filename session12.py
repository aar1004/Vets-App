cafe_name = "John's cafe"
# cafe_name = 'John's cafe'  -> error or use 'John\'s cafe' to use single quotes
print("cafe name is", cafe_name, type(cafe_name), id(cafe_name))
# print("sum", sum(cafe_name)) # will not work
print("min", min(cafe_name))
print("max", max(cafe_name))
print("length", len(cafe_name))

johns_cafe_name = """john's cafe delight
-an authentic italian restaurant
"""
print(johns_cafe_name)

quote = "be \nexceptional"  # escape characters
print(quote)


# raw string -> will ignore all escape sequences and consider it as a part of string
quote = r"be \nexceptional"  # escape characters
print(quote)
