"""Random character by choice"""

import random
import string

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
print("---------------------------------\n")

combination = letters + digits + symbols

user_combination = letters
allow_digits = input("Allow numbers? [y/n]: ").lower()
allow_symbols = input("Allow symbols? [y/n]: ").lower()
password_length = int(input("Enter the length of the password (default is 10): "))

if allow_digits == "y":
    user_combination += digits
if allow_symbols == "y":
    user_combination += symbols

password = ""
for i in range(password_length):
    random_character = random.choice(user_combination)
    password += random_character
print("The random password is:", password)
