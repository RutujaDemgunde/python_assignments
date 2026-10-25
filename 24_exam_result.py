# 24. Check exam result (example scale)
marks = float(input("Enter marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")

# Note: Confirm the result thresholds with your teacher if specified.
