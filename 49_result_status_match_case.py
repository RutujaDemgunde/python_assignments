status = input("Enter result status (pass/fail/ATKT): ").strip().lower()
match status:
    case "pass":
        print("Congratulations! You passed.")
    case "fail":
        print("You need to try again.")
    case "atkt":
        print("You have an ATKT.")
    case _:
        print("Invalid result status.")
