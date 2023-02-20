import random
import string
import pyperclip

def generate_password(length, lowercase=True, uppercase=True, digits=True, special=True):
    chars = ""
    if lowercase:
        chars += string.ascii_lowercase
    if uppercase:
        chars += string.ascii_uppercase
    if digits:
        chars += string.digits
    if special:
        chars += string.punctuation

    password = "".join(random.choice(chars) for _ in range(length))
    pyperclip.copy(password)
    return password


length = int(input("Enter the length of the password: "))
lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
digits = input("Include digits? (y/n): ").lower() == "y"
special = input("Include special characters? (y/n): ").lower() == "y"

password = generate_password(length, lowercase, uppercase, digits, special)
print(f"\nYour generated password: {password}\n\nPassword copied to clipboard!")
