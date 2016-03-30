raw_input("enter score (0~100): ")
Score=raw_input("enter score (0~100): ")
Score=float(Score)


def computeGrade(Score):
    if (90<=Score<=100):
        grade='A'

    elif (80<=Score<90):
        grade='B'

    elif (70<=Score<80):
        grade='C'

    elif (60<=Score<70):
        grade='D' 

    elif (Score<60):
        grade='F'
        
    return grade

computeGrade(90)