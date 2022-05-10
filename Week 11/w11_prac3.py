"""Reading a file"""
file_in = open("data.txt", "r")  # read and stores the content of a file in a variable
print(file_in.read())  # prints the content of a file

"""Adding line from a file to a list"""
fruit = []
for line in file_in:
    fruit.append(line.strip())  # .strip() clears the new lines
print(fruit)
file_in.close()

"""Creating and writing into a file"""
file_out = open("data1.txt", "w")
file_out.write("This is a new line.")
file_out.close()

"""Appending (adding) into a file"""
file_out = open("data1.txt", "a")
file_out.write("\nThis is a new line.")
file_out.close()
