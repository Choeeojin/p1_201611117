import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

t1.home()
t1.clear()





def makeSwirlSqaure(size,bigger,sides,angle):
	for i in range(0,sides):
        	if(i%2):
           	 size=size+bigger
            	t1.forward(size)
            	t1.right(angle)


size=10
bigger=10
sides=20
angle=90


makeSwirlSquare(size,bigger,sides,angle)


wn.exitonclick()