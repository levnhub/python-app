# Conditions

is_happy = False
is_sad = True

if is_happy and not is_sad:
    print("User is happy!")
elif is_happy and is_sad:
    print("User is confused")
else:
    print("User is sad")

# Ternary

data = input()

number = 5 if data == "five" else 0

print(number)

# Other

user_data = int(input("Input number: "))

if user_data > 5:
    print("Number is bigger that 5")
    if user_data == 6:
        print("Number is equal 6")

print("Always print")
