# 17. Check grade based on marks (example grading scale)
marks = float(input("Enter marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")

# Note: Confirm the grade ranges with your teacher if a specific scale was given.
