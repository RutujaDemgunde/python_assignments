# 20. Check ticket price based on age (example prices)
age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")
elif age < 5:
    print("Ticket is free")
elif age < 18:
    print("Ticket price: Rs. 100")
else:
    print("Ticket price: Rs. 200")

# Note: These are example prices; use your teacher's specified prices if provided.
