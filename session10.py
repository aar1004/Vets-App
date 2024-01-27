my_data = [10, 20, 30]  # 1D
numbers = [[10, 20, 30], [40, 50, 60, 70, 80], [90, 99]]  # 2D

print(len(my_data))
print(my_data[1])

print(len(numbers))
print(numbers[1])
print(numbers[1][2])


large_data = [
    [[10, 20, 30], [40, 50, 60, 70, 80], [90, 99]],
    [[10, 20, 30], [40, 50, 60, 70, 80], [90, 99]],
]

print(large_data[1][2][0])

print(my_data[-1])

print(numbers[-2][-1])

print(large_data[-1][-2][-2])


# Slicing
data = list(range(10, 101, 10))  # 10,20,30,40,50,60,70,80,90
print("data", data)
print(data[:5])  # not inclusive

print(data[6:])  # takes index
print("hello", data[5:9])
print("-5", data[:-5])
print("-5 ans -2", data[-5:-2])  # -2 not inclusive
data1 = [10, 20, 30]
data2 = [40, 50, 60]

data3 = data1 + data2
print("data3", data3)  # concatenation

data4 = data1 * 2  # multipilicity
print("data4", data4)

# membership testing

print(10 in data1)
print(100 in data2)
print(100 not in data1)
