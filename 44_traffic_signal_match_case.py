signal = input("Enter traffic signal color (red/yellow/green): ").strip().lower()
match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait and get ready")
    case "green":
        print("Go")
    case _:
        print("Invalid traffic signal color.")
