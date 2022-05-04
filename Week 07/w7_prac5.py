"""https://www.studytafensw.edu.au/lesson?id=343114&page=232927"""

"""For loop with the function range()"""
for number in range(3):  # loops for 3 times
    print(number)

print("\n------------------")  # Just a line separator

for digit in range(1, 4):  # loops from 1 to 3
    print(digit)

print("\n------------------")  # Just a line separator

result = 0
print("Enter 2 number to calculate their sum.")
for question in range(2):
    num = int(input("Enter a number: "))
    result += num
print("The sum is:", result)
