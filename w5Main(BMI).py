"""

@author cej
@since 160404
"""





def BMI(height,weight):
    height=float(1.8)
    weight=float(75)

    bmi=weight/(height*height)

    print bmi



if bmi<18.5:
    print "low weight"
elif 18.5<=bmi<23:
    print "standard"
elif 23<=bmi<25:
    print "overweight"
elif 25<=bmi<30:
    print "obesity"
elif 30<=bmi:
    print "high obesity"
else:
    print "error"


def lab5():
	height=float(1.8)
	weight=float(75)
	BMI(height,weight)

def main():
	lab5()
if __name__=="__main__"
	main()