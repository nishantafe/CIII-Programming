def get_details():
    name = input("Enter your name: ")
    postcode = int(input("Enter your post code: "))
    return [name, age, postcode]


def check_age(age):
    if age > 18:
        print("Adult")
    else:
        print("Minor")


member = input("Are you a member [y/n]: ").lower()

if member == "y":
    print("Welcome our dear member")
else:
    print(get_details())
    age = int(input("Enter your age for verification: "))
    check_age(age)
