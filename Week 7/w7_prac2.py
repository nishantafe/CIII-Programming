# Use a "while loop" to continuously as the user
# to enter a password until they get it right.
# If the get it right congratulates them.

correct_password = "123"
user_entered_password = input("Enter the password: ")

while user_entered_password != correct_password:
    print("Invalid password! Please try again.")
    user_entered_password = input("Enter the password: ")
else:
    print("Congratulations! password is correct")
