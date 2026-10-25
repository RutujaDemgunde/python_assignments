# 12. Check whether a person is a child or adult (adult age is 18 or above)
age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")
elif age < 18:
    print("Child")
else:
    print("Adult")
