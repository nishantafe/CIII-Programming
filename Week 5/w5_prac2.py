# Activity: https://www.studytafensw.edu.au/lesson?id=343093&page=232843

# Pseudocode-------------------------------

# 1.  INPUT a number
# 2.  READ the number
# 3.  IF divisible by 4 THEN
# 4.  DISPLAY The number is divisible by 4
# 5.  END IF
# 6.  IF divisible by 2 THEN
# 7.  DISPLAY The number is divisible by 2
# 8.  END IF
# 9.  IF number is odd THEN
# 10. DISPLAY The number is odd
# 11. END IF

# Python ----------------------------
number = int(input("Enter a number to get its properties: "))

if number % 4 == 0:
    print(number, "is divisible by 4")

elif number % 2 == 0:
    print(number, "is divisible by 2")

if number % 2 != 0:
    print(number, "is an odd number")
