number = input("Enter a number: ")

try:
    number = int(number)
    is_number = True
except:
    is_number = False

print("is_number: ", is_number)

if is_number:
    print("Well done! that's a number")
    total = number + 10
    print("I added 10 to your number and now it's:", total)
else:
    print("Error: That's not a number, could not calculate")
