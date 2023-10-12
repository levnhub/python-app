# Tuple

data = (4, 6, 8, True, 5.6, "Hello")  # tuple
# data[0] = 1 # TypeError: 'tuple' object does not support item assignment
print(data)
print(data[2:5])

print(data.count(6))  # 1
print(len(data))  # 1

new_data = 5, 6, 9, 10, "tuple"
print(new_data)

new_data_2 = 5  # not tuple
new_data_3 = (5,)  # tuple
new_data_4 = (5,)  # tuple

# Tuple Loop

for item in data:
    print(item)

# List to tuple

list = [1, 2, 3]
new_tuple = tuple(list)
print(new_tuple)

# String to tuple

word = "Hello"
print(tuple(word))
