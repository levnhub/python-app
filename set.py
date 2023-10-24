# Set by method

# data = set("hello")

data = {5, 7, 6, 7}

data.add(32)
data.update([True, 4, 6])
data.remove(True)
data.pop()
data.clear()

nums = [5, 7, 3, 5, 5]
nums = set(nums)

new_data = frozenset([5, 7, 6, 7, True, 4, 5, 7, 3, 5, 5])
# new_data.add(1) # error

print(data)
print(nums)
print(new_data)
