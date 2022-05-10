number = input("Enter a number: ")

try:
    number = int(number)
    is_number = True
except:
    is_number = False

while not is_number:
    print("Error: That's not a number, could not calculate")
    number = input("Enter a number: ")
    try:
        number = int(number)
        is_number = True
    except:
        is_number = False

    else:
        print("Well done! that's a number")
        total = number + 10
        print("I added 10 to your number and now it's:", total)
