# https://www.studytafensw.edu.au/lesson?id=343114&page=232969
# Create a new list of objects
# in this case, car parts

carParts = ["CV Joint", "spark plug", "air filter",
            "timing belt", "piston", "brake pad", "ball joint"]
print(carParts)
# You can remove items from a list using the .remove() function
# Lets remove the "brake pad" object from the list which is at
# index 5 ['CV Joint', 'spark plug', 'air filter', 'timing belt', 'piston', 'brake pad', 'ball joint']
carParts.remove(carParts[5])

print(carParts)

# use index() to get the index number or an item in a list
print(carParts.index("spark plug"))