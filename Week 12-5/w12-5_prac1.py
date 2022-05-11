my_dictionary = {"John": "045215879", "Mary": "045234358"}

# Access the value of a certain key
value = my_dictionary.get("John")
print("value: ", value)

# Access Items
print(my_dictionary.keys())  # Access keys
print(my_dictionary.values())  # Access values

if "John" in my_dictionary.keys():
    print("John is in the dictionary")
if "045215879" in my_dictionary.values():
    print("045215879 is in the dictionary")

# Add item
my_dictionary["David"] = "045123854"
print(my_dictionary)
