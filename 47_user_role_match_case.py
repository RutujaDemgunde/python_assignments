role = input("Enter role (admin/user/guest): ").strip().lower()
match role:
    case "admin":
        print("Welcome, Admin. You have full access.")
    case "user":
        print("Welcome, User. You have standard access.")
    case "guest":
        print("Welcome, Guest. You have limited access.")
    case _:
        print("Unknown role.")
