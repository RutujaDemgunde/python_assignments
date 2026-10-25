# 30. Check whether a number is single-digit, double-digit, or three-digit
num = int(input("Enter an integer: "))
value = abs(num)

if value <= 9:
    print("Single-digit number")
elif value <= 99:
    print("Double-digit number")
elif value <= 999:
    print("Three-digit number")
else:
    print("More than three digits")
