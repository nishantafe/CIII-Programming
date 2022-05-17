number = input("Input a number: ")
while True:  # Keep looping
    try:
        number = int(number)  # Try casting to an integer
        is_num = True
        break  # Exit the loop
    except:
        number = input("Input a number: ")
print(number, is_num)
