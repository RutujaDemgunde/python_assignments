password = input("Enter a password: ")

if len(password) >= 8:
    if any(char.isalpha() for char in password):
        if any(char.isdigit() for char in password):
            print("Valid password.")
        else:
            print("Invalid password: include at least one digit.")
    else:
        print("Invalid password: include at least one letter.")
else:
    print("Invalid password: it must contain at least 8 characters.")
