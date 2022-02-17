# input() function gets an entry from a user
# input("Your question") put the question inside input() surrounded by brackets
name = input("Enter your name: ")

# int() casts/converts data type into an integer
age = int(input("Enter your age: "))

# print(name)
# print(type(age))

age_next_year = age + 1

print("Hello", name, "you are", age)
print("Next year you'll be", age_next_year)
