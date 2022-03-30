"""https://www.studytafensw.edu.au/lesson?id=343114&page=232934"""

# If it does not rain tomorrow and the trains are on time
    # I will ride my pushbike to the station.
# If it does not rain and the trains are early
    # I will drive my car to the station
# If it rains tomorrow
    # I will not go to work

raining = input("Please enter True or False if it will rain tomorrow: ")
trainsOnTime = input("Will the trains be on time? Enter – Yes, Early, Late: ")
# Convert the user's response to a bool
# Here we're re-assigning the type of variable 'raining'
if raining == "False" and trainsOnTime == "Yes":
    print("I will ride my pushbike to the station.")
elif raining == "False" and trainsOnTime == "Early":
    print("I will drive my car to the station!")
elif raining == "True" and trainsOnTime == "Late":
    print("I will NOT go to Work!", raining, trainsOnTime)
else:
    print("I will go to work as usual!")

