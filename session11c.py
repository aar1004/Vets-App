# for each or enhanced for loop
data = list(range(10, 101, 10))
print(data)
"""for idx in range(len(data)):
    print(data[idx])"""

data = set(data)

for element in data:  # set par for each loop work kar sakta hai
    print(element)

student = {"rollno": 101, "name": "fionna", "age": 21}

items = student.items()
for item in items:
    print(item)

# for keys ->  print(item[0])
# for values ->   print(item[1])

keys = student.keys()
for key in keys:
    print(key)


print("dictionary key and values")
for key in student:
    print(key, student[key])
