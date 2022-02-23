# See the deference between the results of the 2 following lines:
print((5 + 5) * (5 + 5))
print(5 + 5 * 5 + 5)

# use % to find if a number is even or odd
number = int(input("Enter a number to find if it's even or odd: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
