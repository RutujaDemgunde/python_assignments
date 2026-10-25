# 9. Check whether a student has passed or failed (pass marks = 40)
marks = float(input("Enter marks: "))

if 0 <= marks <= 100:
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Invalid marks. Enter marks from 0 to 100.")
