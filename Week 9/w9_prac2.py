names = ["John", "Samuel", "Samantha", "Veronica", "Christopher", "Alessandro"]
ages = [33, 103, 13, 27, 23, 21]

# getting an element from a list by its index (number while the first is 0)
print(names[2])  # Samantha
print(ages[2])  # 13
print("---------------------")

# len() gets you the length/count of elements in a list
print("Count of names is:", len(names))
print("---------------------")

# using the variable i to dynamically get each element from multiple lists
# by using a for loop
for i in range(len(names)):
    print(names[i], ages[i])
    # print("{:15s} {}".format(names[i], ages[i]))

