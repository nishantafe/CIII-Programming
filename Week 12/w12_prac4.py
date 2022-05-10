number = input("Input a number: ")

while number != int:
    try:
        number = int(number)
        is_num = True
        break
    except:
        number = input("Input a number: ")
print(number, is_num)