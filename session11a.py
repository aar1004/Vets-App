# explore set
john_followers = {"fionna", "sia", "jack", "joe", "george"}
print(john_followers)  # any order because it works on hashing
print(type(john_followers))
numbers = list(range(10, 101, 10))
print(numbers, type(numbers))
numbers = set(numbers)
print("numbers now", numbers, type(numbers))
numbers.add(10)  # will not be added
numbers.add(110)
numbers.add(220)
numbers.add(20)  # will not be added
print(numbers)
numbers.pop()  # front se remove hoga
numbers.pop()
print("after pop", numbers)
numbers.remove(50)
print("numbers after remove", numbers)
numbers.discard(90)
print("numbers after discard", numbers)  # works same as remove


john_followers = {"fionna", "sia", "jack", "joe", "george"}
jake_followers = {"anna", "kim", "leo", "joe", "harry", "mike", "jack"}
fionna_followers = {"sia", "joe"}

followers = john_followers.intersection(jake_followers).intersection(fionna_followers)
print("mutual followers", followers)

print(fionna_followers.issubset(john_followers))
print(john_followers.issuperset(fionna_followers))

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = a - b
print("c is", c)

d = a & b
print("d is", d)

e = a ^ b
print("e is", e)
f = a | b
print("f is", f)

g = a.symmetric_difference(b)
print("g is", g)
a.clear()
