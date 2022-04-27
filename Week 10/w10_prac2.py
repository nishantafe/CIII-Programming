"""https://www.studytafensw.edu.au/lesson?id=343114&page=232997"""

import math
import string
import random
import time

my_pi = math.pi
print(my_pi)

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

print(letters)
print(digits)
print(symbols)

print("------------------------------------")

print("This program will count the number of letters, digits and symbols in any give word")
word = input("Enter a word: ")
letters_count = 0
digits_count = 0
symbols_count = 0

for letter in word:
    if letter in letters:
        letters_count += 1
    if letter in digits:
        digits_count += 1
    if letter in symbols:
        symbols_count += 1
print("Letters count = ", letters_count)
print("Digits count = ", digits_count)
print("Symbols count = ", symbols_count)

#
# if "!" in symbols:
#     print("found")
# else:
#     print("not found")

for i in range(20):
    time.sleep(10)
    random_number = random.randint(1, 10)
    print("The random number is: ", random_number)
