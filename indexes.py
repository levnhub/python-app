# Slices

word = 'Futurism'

print(word[0:4]) # Futu
print(word[0:-1]) # Futuris
print(word[0:-1:2]) # Ftrs (with step)

list = [6, 4, 'string', True, 6.5]

print(list[2:]) # ['string', True, 6.5]
print(list[::-1]) # [6.5, True, 'string', 4, 6] (sort hack)

