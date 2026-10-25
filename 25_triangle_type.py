# 25. Check whether a triangle is equilateral, isosceles, or scalene
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid triangle sides")
elif a + b <= c or a + c <= b or b + c <= a:
    print("These sides do not form a triangle")
elif a == b == c:
    print("Equilateral triangle")
elif a == b or a == c or b == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
