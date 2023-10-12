# loop

# for
print("# for")

for i in range(1, 6, 2):  # start, end, step
    print(i)

count = 0
word = "Hello!"
for i in word:
    if i == "l":
        count += 1

print("Count: ", count)

# while
print("# while")

i = 5
while i < 15:
    print(i)
    i += 2

# is_has_car = True
# while is_has_car:
#     if input('Enter data: ') == 'stop':
#         is_has_car = False

for i in range(1, 10):
    if i == 5:
        break

    if i % 2 == 0:
        continue

    print(i)

# find symbol in string

found = None
for i in "Hello":
    if i == "l":
        found = True
        break
else:
    found = False

print("Found: ", found)
