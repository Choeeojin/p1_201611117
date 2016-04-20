"""
@author cej
@since 160420
"""

import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def drawSquareFrom(size):
    tracks=dict({1:(size,0),2:(size,-size),3:(0,-size),4:(0,0)})
    for i in range(1,5):
        t1.goto(tracks[i])

drawSquareFrom(100)

wn.exitonclick()

def lab7():
	drawSquareFrom(100)

def main():
	lab6()

if __name__=="__main__":
	main()