"""https://www.studytafensw.edu.au/lesson?id=343086&page=232703"""
# Variable Scope

greeting = "Hello"  # Global variable


def greeting_world():
    """Function to print a greeting"""
    world = "World"  # Local variable
    print(greeting, world)


def greeting_name(name):
    print(greeting, name)

# TODO work on this next time
greeting_world()
greeting_name("Sam")


try:
    surname = "Smith"
except:
    print("Error")

print(surname)