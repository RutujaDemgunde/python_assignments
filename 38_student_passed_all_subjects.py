maths = float(input("Enter marks in Maths: "))
science = float(input("Enter marks in Science: "))
english = float(input("Enter marks in English: "))
passing_marks = 35

if maths >= passing_marks and science >= passing_marks and english >= passing_marks:
    print("The student passed all subjects.")
else:
    print("The student did not pass all subjects.")
