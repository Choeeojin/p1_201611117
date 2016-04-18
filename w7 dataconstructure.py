"""
@author cej
@since 1604018
"""


tracks=list()

def drawSquareAtSave(size):
    t1.home()
    t1.clear()
    for i in range(4):
        t1.forward(size)
        t1.right(90)
        t1.pos()
        tracks.append(t1.pos())
    return tracks

drawSquareAtSave(100)

print tracks





def lab7():
	drawSquareAtSave(size)


def main():
	lab7()
if __name__=="__main__"
	main()