names = "john,jennie,jim,jack,joe"
print("names", names)
names.upper()
print(
    "names now", names
)  # strings are immutable so do this we need to create a new string

upper_case_names = names.upper()  # //ly lower()
print(
    "upper case names now", upper_case_names
)  # new string is created in the memory id will be different
# print("upper case names check", upper_case_names.isupper())


s1 = names.capitalize()
s2 = names.title()
s3 = names.swapcase()
s4 = names.replace("j", "ko")
print("s1", s1)
print("s2", s2)
print("s3", s3)
print("s4", s4)

password = input("enter your password:")
print("password", password.strip())  # //ly rstrip and lstrip

data = "000vsghjs000"
print("data", data.strip("0"))


number = 3.64000
number = float(str(number).strip("0"))
print(number, type(number))

message = "no internet connection"
print(message)
print(message.center(120))
print(message.ljust(120))
print(message.rjust(50))

data = "545"
print(data.zfill(20))

quote = "search the candle rather than cursing the darkness"
print(quote.find("sing"))
print(quote.find("the"))
print(quote.index("the"))
print(quote.rindex("the"))
# for ch in quote:
#     print(ch, end=" ")


idx = quote.index("candle")
idx2 = idx + len("candle") - 1
print(idx)
print(idx2)

print(quote[idx:idx2])

print(len(names))  # 24
print(names[1])  # o
print(names[len(names) - 1])  # e


split_names = names.split(",")
print(split_names, type(split_names))

names.replace("jim", "mike")  # strings are immutable
print(names)

s1 = names.replace("jim", "mike")
print(s1)
