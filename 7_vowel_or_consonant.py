# 7. Check whether a character is a vowel or consonant
ch = input("Enter one alphabet: ")

if len(ch) == 1 and ch.isalpha():
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input. Please enter one alphabet.")
