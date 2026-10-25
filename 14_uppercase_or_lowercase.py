# 14. Check whether a character is uppercase or lowercase
ch = input("Enter one alphabet: ")

if len(ch) == 1 and ch.isalpha():
    if ch.isupper():
        print("Uppercase")
    else:
        print("Lowercase")
else:
    print("Invalid input. Please enter one alphabet.")
