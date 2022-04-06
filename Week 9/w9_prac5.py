# Create a new list of objects
# in this case, car parts

carParts = ["CV Joint", "splat plug", "timing belt",
            "piston", "brake pad", "ball joint"]
print(carParts)

# Oops "splat plug" is not correct. You
# access that object in the list and modify it
# "splat plug" is at index 1

carParts[1] = "something else"
print("\n", carParts)
