data = input("Input text: ")

# file = open("data/text.txt", "w")  # rewrite
file = open("data/text.txt", "a")  # append

file.write(data + "\n")

file.close()

newFile = open("data/text.txt", "r")

print(newFile.read(3))  # argument for return symbols count

for line in newFile:
    print(line, end="")  # remove unwanted extra new lines

newFile.close()
