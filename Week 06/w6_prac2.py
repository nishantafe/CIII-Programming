name = input("Enter your name: ")

# only one possibility will apply with elif
if (name == "Nishan") or (name == "Jordan"):
    print("Hi", name, "you have full access")
elif name == "Sam":
    print("Your access has expired!")
else:
    print("Access denied!")
