my_dictionary = {}
# Read from file
file_in = open("data.txt", "r")
for line in file_in:
    key, value = line.split(" ")
    my_dictionary[key] = value.strip()
print("my_dictionary is: ", my_dictionary)
file_in.close()

# Add item to dictionary
my_dictionary["David"] = "045123854"

# Appending to a file
file_out = open("data.txt", "a")
user = "David"
file_out.write("\n" + user + " " + my_dictionary[user])

# New Dictionary
new_dictionary = {"user1": "password1", "user2": "password2"}
user = "user2"
password = new_dictionary[user]
print(user, password)

# add user
new_dictionary["user3"] = "password3"
print(new_dictionary)
