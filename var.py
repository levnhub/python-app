# Vars

number = 5 # int

digit = 4.534324 # float
word = "Result: " # string
boolean = True # bool
str_num = "5"

# Types modify

print(word + str(digit))
print(word + str(number + int(str_num)))

del number 

number = 7

print(word, number)

# Input operations

num1 = int(input('Input first number: '))
num2 = int(input('Input second number: '))

# num1 += 5
# num1 -= 5
# num1 /= 5
# num1 *= 5

print(word, num1 + num2)
print(word, num1 - num2)
print(word, num1 / num2)
print(word, num1 * num2)
print(word, num1 ** num2)
print(word, num1 // num2)

str = 'Hi'
print(str * 2) # HiHi
