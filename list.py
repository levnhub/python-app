# list methods 1

nums = [5, 2, 7, 9, True, 'Hello', 2.1, [5, 7]]

nums[0] = 50

print(nums)
print(nums[-1][1]) # 7

nums.append(100)
nums.insert(1, 200) # [5, 200, ...]
nums_new = [6,7,8]
nums.extend(nums_new)
# nums.sort() # error

print(nums)

# list methods 2

some_nums = [8,5,4,7]
some_nums.sort()
# some_nums.reverse()
some_nums.pop() # remove last
some_nums.pop(0) # remove index
some_nums.remove(7) # remove value
# some_nums.clear() # remove all

print(some_nums)
print(some_nums.count(5)) # 1
print(len(some_nums)) # 1

# list loop

nums = [5, 2, 7, '50', False]

for el in nums:
    el *= 2
    print(el)

# list input program

n = int(input('Enter length: '))

user_list = []

i = 0
while i < n:
    label = 'Enter element #' + str(i + 1) + ': '
    user_list.append(input(label))
    i += 1

print(user_list)