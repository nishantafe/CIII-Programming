x = 10
y = "man"

# result = x + y
# print(result)
print(type(y))  # print the data-type of a variable using the function type()

try:
    print(number)
except NameError:
    print("Sorry that variable does not exist")

try:
    result = x + y
except TypeError:
    print("Could not perform the calculation")

try:
    result = x + y
except:
    print("Could not perform the calculation")
