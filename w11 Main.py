import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def drawLine():
    t1.penup()
    t1.setpos(-100,0)
    t1.pendown()
    t1.forward(100)
    t1.penup()
    t1.home()

drawLine()

x=list()
for i in range(-100,0):
    x.append(i)
if t1.pos(x[i],0):
    print "t1 on Line"
else:
    print "Keep going"


def keyup():
    t1.forward(50)
def keydown():
    t1.back(50)
def keyright():
    t1.right(90)
def keyleft():
    t1.left(90)
def keybye():
    wn.bye()

def mousegoto(x,y):
    t1.setpos(x,y)

def addkeys():
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down")
    wn.onkey(keyright,"Right")
    wn.onkey(keyleft,"Left")
    wn.onkey(keybye,"q")

def addMouse():
    wn.onclick(mousegoto)

addMouse()
addkeys()
wn.listen()
turtle.mainloop()

