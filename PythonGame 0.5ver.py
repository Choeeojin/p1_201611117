import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.home()
t1.clear()
t1.penup()



def k1():
	move.forward(45)

def k2():
	move.left(45)

def k3():
	move.right(45)

def k4():
	move.back(45)

wn.onkey(k1, "Up")
wn.onkey(k2, "Left")
wn.onkey(k3, "Right")
wn.onkey(k4, "Down")



wn.exitonclick()