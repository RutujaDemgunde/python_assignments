# 29. Check blood donation eligibility based on age and weight
age = int(input("Enter age: "))
weight = float(input("Enter weight in kg: "))

if age >= 18 and weight >= 50:
    print("May meet the basic age and weight criteria; consult a blood donation centre.")
else:
    print("Does not meet the example age and weight criteria.")

# Note: Eligibility depends on local rules and a medical screening.
