# multi value containers

# explore list in python
numbers = list(range(10, 101, 10))
print("1", numbers)
print(type(numbers))
numbers.append(30)
numbers.append(77)
numbers.append(99)
print("2", numbers)
print("sum", sum(numbers))
print("min", min(numbers))
print("max", max(numbers))
print("length", len(numbers))
reverse_numbers = list(reversed(numbers))
print("reversed list", reverse_numbers)
print(numbers.index(50))
print("count of 30 in numbers is", numbers.count(30))
data = [70, 30, 50, 90, 20]
print("data is", data)
data.sort()
print("data in sorted way", data)
names = ["john", "anna", "sia", "angel", "kia"]
names.sort()  # alphabetical sort
print(names)
print("min", min(names))
print("max", max(names))
# print("sum", sum(names))  # error

names.remove("sia")
print(names)

data = [10, 20, 30, 40, 50]  # list can be used as stack
# data.pop()
# print(data)

# data.pop(0)  # list can be used as a queue
# print(data)

# data.clear()
# print(data)

data.insert(2, 77)
print(data)
# data.insert(99)#error
data.insert(len(data), 100)  # len(data)-1 bhi second last par karega
print(data)
data.insert(-1, 78)  # second last mein add kiya hai
print(data)
