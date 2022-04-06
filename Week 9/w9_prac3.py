text = "Hello"
names = ["John", "Samuel", "Samantha"]
ages = [33, 103, 13]

print(names[2], "is", ages[2], "years old")  # Samantha is 13 years old

print("----------------------------")
print("First 3 ages:")
print(ages[0])  # 33
print(ages[1])  # 103
print(ages[2])  # 13

print("----------------------------")
print("Count of names:")
print(len(names))  # 3

print("----------------------------")
print("Loop to get the names and ages dynamically:")
for i in range(len(names)):
    print(names[i], ages[i])

print("----------------------------")
print("Adding a new name...")
# append() adds an item to a list"
names.append("Jax")
ages.append("36")

print("----------------------------")
print("Loop to get the names and ages dynamically:")
for i in range(len(names)):
    print(names[i], ages[i])
