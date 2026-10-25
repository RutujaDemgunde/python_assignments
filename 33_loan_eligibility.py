age = int(input("Enter your age: "))
monthly_income = float(input("Enter your monthly income (Rs.): "))
credit_score = int(input("Enter your credit score: "))

if age >= 21 and monthly_income >= 25000 and credit_score >= 650:
    print("You can apply for a loan.")
else:
    print("You are not eligible to apply for a loan based on these criteria.")
