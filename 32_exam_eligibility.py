# 32. Check whether a student is eligible for an exam (attendance + marks)
attendance = float(input("Enter attendance percentage: "))
marks = float(input("Enter marks: "))

if 0 <= attendance <= 100 and 0 <= marks <= 100:
    if attendance >= 75 and marks >= 40:
        print("Eligible for exam")
    else:
        print("Not eligible for exam")
else:
    print("Invalid input")

# Note: Attendance and marks criteria are examples; use your teacher's rules if provided.
