# Page https://www.studytafensw.edu.au/lesson?id=343114&page=232906

order = input("Would you like a pizza or eggs?: ").lower()
if order == "eggs":
    print("You chose eggs yummy!")
    egg_type = input("Would you like them boiled of fried? ")
    if egg_type == "boiled":
        print("Boiled eggs are coming right up")
    elif egg_type == "fried":
        print("Fried eggs are coming right up")
    else:
        print("Sorry we don't make", egg_type, "eggs")

elif order == "pizza":
    pizza_type = input("Would you like a Vegetarian or Hawaiian pizza?").lower()
    if pizza_type == "vegetarian":
        print("Vegetarian pizza is coming right up")
    elif pizza_type == "hawaiian":
        print("Hawaiian pizza is coming right up")
    else:
        print("Sorry we don't make", pizza_type, "pizza")

else:
    print("Sorry we ran out of", order, "today.")
