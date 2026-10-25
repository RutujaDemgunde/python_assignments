# 23. Calculate electricity bill based on units consumed (example slabs)
units = float(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 3
    print("Electricity bill: Rs.", round(bill, 2))
elif units <= 200:
    bill = (100 * 3) + ((units - 100) * 5)
    print("Electricity bill: Rs.", round(bill, 2))
else:
    bill = (100 * 3) + (100 * 5) + ((units - 200) * 8)
    print("Electricity bill: Rs.", round(bill, 2))

# Note: Example rates only. Replace them with the rates given by your teacher.
