# 28. Calculate discount based on total shopping amount (example rates)
amount = float(input("Enter total shopping amount: Rs. "))

if amount < 0:
    print("Invalid amount")
elif amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
elif amount >= 1000:
    discount = amount * 0.05
else:
    discount = 0

if amount >= 0:
    final_amount = amount - discount
    print("Discount: Rs.", round(discount, 2))
    print("Final amount: Rs.", round(final_amount, 2))

# Note: Example discount rates only. Use your teacher's rules if provided.
