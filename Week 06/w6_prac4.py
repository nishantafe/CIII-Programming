subjectFinalMark = int(input("Please enter the student's Subject Final Mark: "))

if(subjectFinalMark < 0) or (subjectFinalMark > 100):       # grades outside range of 0 to 100
    print("Please enter values from 0 to 100.")
elif (subjectFinalMark >= 0) and (subjectFinalMark < 50):   # grades from 0 to 49
    print("The student's Final Grade is FAIL!")
elif subjectFinalMark < 60:                               # grades form 50 to 59
    print("The student's Final Grade is PASS!")
elif subjectFinalMark < 75:                               # grades from 60 to 74
    print("The student's Final Grade is CREDIT!")
elif subjectFinalMark < 85:                               # grades from 75 to 84
    print("The student's Final Grade is DISTINCTION!")
elif subjectFinalMark <= 100:                             # grades from 85 to 100
    print("The student's Final Grade is HIGH DISTINCTION!")
