# Create a new list of objects
# in this case, car parts

carParts = ["CV Joint", "spark plug", "timing belt",
            "piston", "brake pad", "ball joint"]
print(carParts)

# You can insert an object into a list using the insert function. The insert
# function takes two arguments. The index of the position you'd like to
# insert at and the object you'd like to insert.

carParts.insert(2, "air filter")

print(carParts)
