x = 0

while x == 0:
    try:
        x = int(input("Input number: "))
        x *= 5
        print(x)
    except ValueError:
        print("Bad number")

try:
    x = 5 / 0
except ZeroDivisionError:
    print("Zero division error")
except ValueError:
    print("Value bad")
else:
    print("Some else code")
finally:
    print("Final")
