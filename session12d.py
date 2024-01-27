name = "john"
age = 40
email = "john@example.com"

print(name, age, email)

# string formatting

print("name", name, "age:", age, "email:", email)

print("name:{} age:{} email:{}".format(name, age, email))
print("name:{1} age:{2} email:{0}".format(name, age, email))
print("name:{nm} age:{ag} email:{em}".format(nm=name, ag=age, em=email))

contact = {"name": "john", "age": 40, "email": "john@example.com"}


print("name:{name} age:{age} email:{email}".format_map(contact))
