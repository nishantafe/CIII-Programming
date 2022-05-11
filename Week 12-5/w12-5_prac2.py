phonebook = {}
file_in = open("data.txt", "r")
for line in file_in:
    # store the key and value after extracting them for a line by splitting them using space
    key, value = line.split(" ")
    # Add the pair (key, value) to the dictionary. Uses strip() to get rid of the new line (\n)
    phonebook[key] = value.strip()

# Ask the user to enter a name
# check if the name exists in the dictionary
# print a response
user_name = input("Enter your name: ")
user_phone = input("Enter your phone number: ")

if (user_name in phonebook.keys()) and (user_phone == phonebook.get(user_name)):
    print("Welcome", user_name)
else:
    print("Sorry your name is not in the list.")
print("thanks")
file_in.close()
