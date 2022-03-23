name = "James"  # Data type is: String
number = 10  # Data type is: Integer
height = 1.6  # Data type is: Float

names = ["Jordan", "Brett", "Tristan"]  # Data type is: List
numbers = [10, 20, 30]  # Data type is: List
heights = [1.5, 1.6, 1.7]  # Data type is: List

print(*names)  # adding * before the list name, prints list items
               # seperated by space which is the default seperator of print()

print(*names, sep="\n")  # you can alter the seperator to be a new line \n
                         # which lets you print items under each other.

# We use the function append() to add an item to a list
names.append("Jaz")
print(names)

# We use the function remove() to remove an item from a list
names.remove("Jaz")
print(names)
