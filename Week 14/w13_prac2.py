print("please enter your 5 marks below")

# read 5 inputs
mark1 = int(input("enter mark 1: "))
mark2 = int(input("enter mark 2: "))
mark3 = int(input("enter mark 3: "))
mark4 = int(input("enter mark 4: "))
mark5 = int(input("enter mark 5: "))
if ():  # mark1 <= 0 or mark2 <= 0...
    print("Negative marks are not allowed")
elif ():  # mark1 > 100 or mark2 > 100...
    print("Marks greater than 100 are not allowed")
else:

    # create array/list with five marks
    marksList = [mark1, mark2, mark3, mark4, mark5]

    # print the array/list
    print(marksList)

    # calculate the sum and average
    sumOfMarks = sum(marksList)
    averageOfMarks = sum(marksList) / 5

    # display results
    print("The sum of your marks is: " + str(sumOfMarks))
    print("The average of your marks is: " + str(averageOfMarks))
