my_data = (10, 20, 30)
print(len(my_data))
print(my_data[1])
numbers = ((10, 20, 30), (40, 50, 60, 70, 80), (90, 99))
print(len(numbers))
print(numbers[1])
print(numbers[1][2])

large_data = (
    ((10, 20, 30), (40, 50, 60, 70, 80), (90, 99)),
    ((10, 20, 30), (40, 50, 60, 70, 80), (90, 99)),
)
print(large_data[1][2][0])
data = tuple(range(10, 101, 10))  # 10,20,30,40,50,60,70,80,90
print("data", data)
print(data[:5])  # not inclusive

print(data[6:])  # takes index
print("hello", data[5:9])
print("-5", data[:-5])
print("-5 ans -2", data[-5:-2])

data1 = (10, 20, 30)
data2 = (40, 50, 60)

data3 = data1 + data2
print("data3", data3)

data4 = data1 * 2  # multipilicity
print("data4", data4)

print(10 in data1)
print(100 in data2)
print(100 not in data1)
