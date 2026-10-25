balance = 5000.0
print("ATM Menu")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
choice = int(input("Enter your choice (1-3): "))

match choice:
    case 1:
        print("Your balance is Rs.", balance)
    case 2:
        amount = float(input("Enter amount to deposit: Rs. "))
        if amount > 0:
            balance += amount
            print("Deposit successful. New balance: Rs.", balance)
        else:
            print("Enter a valid deposit amount.")
    case 3:
        amount = float(input("Enter amount to withdraw: Rs. "))
        if amount <= 0:
            print("Enter a valid withdrawal amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print("Withdrawal successful. New balance: Rs.", balance)
    case _:
        print("Invalid choice.")
