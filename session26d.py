def fetch():
    file = open("ipl-data-2022.csv", "r")

    # list of strings
    lines = file.readlines()

    for line in lines:
        # if a function yields,it means we get generator in return
        # as will as we can fetch it line by line
        yield line
        # return line  -> only one line will be executed


result = fetch()
print("result:", result)

# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result), "no more data")

while True:
    data = next(result, "nothing")
    print(data)
    if data == "Nothing":
        break
