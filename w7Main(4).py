﻿"""
@author cej
@since 160420
"""



import turtle
wn=turtle.Screen()
wn.bgpic("myMaze.gif")
t1=turtle.Turtle()



def saveTracks():
    tracks=list()
    tracks.append(t1.pos)
    t1.speed(1)
    t1.penup()
    t1.goto(-400,300)
    t1.pendown()
    t1.pencolor("Red")
    t1.right(90)
    t1.fd(400)
    t1.backward(150)
    t1.left(90)
    t1.fd(300)
    t1.left(90)
    t1.fd(300)
    t1.back(150)
    t1.right(90)
    t1.fd(300)
    t1.left(90)
    t1.right(90)
    t1.right(90)
    t1.fd(200)
    t1.fd(300)
    t1.back(100)
    t1.left(90)
    t1.fd(200)

def lab7():
	saveTracks()


def main():
	lab7()
if __name__=="__main__"
	main()