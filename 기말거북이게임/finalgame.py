```
created by eojin
python game 1.0ver

```


import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
wn.bgpic("Game.gif")

def drawSquare(size,angle,side):
    for i in range(side):
        t1.fd(size)
        t1.right(angle)

def realSquare(pos,coord):
    x=pos[0]
    y=pos[1]
    x1=coord[0][0]
    y1=coord[0][1]
    x2=coord[1][0]
    y2=coord[1][1]
    
    if (x>x1 and x<x2) and (y>y1 and y<y2):
        t1.clear()
        wn.bgpic("win.gif")
        print "You want guit the Game, Press 'q'"
    else:
        print "Keep Going"

def keyup():
    t1.forward(50)
    realSquare(t1.pos(),[(50,-100),(150,0)])
def keydown():
    t1.back(50)
def keyright():
    t1.right(90)
def keyleft():
    t1.left(90)
def keybye():
    wn.bye()

def addkeys():
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down")
    wn.onkey(keyright,"Right")
    wn.onkey(keyleft,"Left")
    wn.onkey(keybye,"q")

def labfinal():
    t1.home()
    t1.clear()
    t1.pencolor("White")
    t1.penup()
    t1.goto(-150,0)
    t1.pendown()
    drawSquare(100,90,4)
    t1.penup()
    t1.goto(50,0)
    t1.pendown()
    drawSquare(100,90,4)
    t1.penup()
    t1. goto(0,100)
    t1.right(90)
    t1.shape("turtle")
    addkeys()
    wn.listen()
    turtle.mainloop()
    wn.exitonclick()

def main():
    labfinal()

if __name__=="__main__":
	main()
