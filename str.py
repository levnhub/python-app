# String

word = "mashina"
sentense = "terrorism,futurism,realism"

print(word[2])
print(len(word))
print(word.upper())  # MASHINA
print(word.isupper())  # False
print(word.find("s"))  # 2
interest = sentense.split(",")
print(interest[1])

# Mutate array

for i in range(len(interest)):
    interest[i] = interest[i].capitalize()

print(interest)

result = ", ".join(interest)  # Terrorism, Futurism, Realism

print(result)
