# 22. Check salary bonus based on years of service (example rule)
salary = float(input("Enter salary: Rs. "))
years = float(input("Enter years of service: "))

if years < 0 or salary < 0:
    print("Invalid input")
elif years >= 10:
    bonus = salary * 0.10
    print("Bonus (10%): Rs.", round(bonus, 2))
elif years >= 5:
    bonus = salary * 0.05
    print("Bonus (5%): Rs.", round(bonus, 2))
else:
    print("No bonus")

# Note: Example policy only. Confirm the bonus rules with your teacher.
