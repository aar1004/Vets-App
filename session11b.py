my_tuple = ()
print(my_tuple, type(my_tuple))


my_list = []
print(my_list, type(my_list))

my_set = {}  # it is dictionary to make set {my_set=set()}
print(my_set, type(my_set))

my_dict = dict()  # or can be made using {}
print(my_dict, type(my_dict))

my_data = {101: "john", 201: "fionna", 301: "george", 661: "harry"}
print(my_data)
print("sum", sum(my_data))
print("min", min(my_data))
print("max", max(my_data))
print("length", len(my_data))

print("using square brackets", my_data[201])
print(my_data.get(201))

my_data.pop(201)
print("after pop", my_data)
# remove does not exist


my_data[775] = "leo"
print("adding", my_data)

my_data[775] = "kim"
print("updation", my_data)

del my_data[775]

columns = ["from", "to"]
flights = {}.fromkeys(columns, "delhi")
print(flights)

columns = ["ludhiana", "ferozepur", "moga", "jalandhar", "bhatinda"]
population = {}.fromkeys(columns, 1200)
print(population)


population["ferozepur"] = 3100
print(population)

items = population.items()
print("items", items)

# convert dictionary into list of tuples
items = list(population.items())
print("items", items)
