number = input("enter the number: ")
print("Will not work for large numbers")
print("Will not work for Decimal numbers")
print("Will not work for strings")

if int(number) % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
