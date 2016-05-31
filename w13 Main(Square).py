import os
mydir=os.getcwd()
filename='Square.txt'
myfile=open('Square.txt')
myfn=os.path.join(mydir,filename)
print myfile

%%writefile Square.txt
0,0,100,100
150,150,200,200

fs=open('Square.txt','r')
myfs=[]
for line in fs:
   line1=line.split(',')
   aRect=[(line1[0],line1[1]),(line1[2],line1[3].strip())]
   myfs.append(aRect)
fs.close()

def drawSquareWithFs():
    for xy in myfs:
        x1=int(xy[0][0])
        y1=int(xy[0][1])
        x2=int(xy[1][0])
        y2=int(xy[1][1])
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    print x1,y1,x2,y2
    for i in range(4):
        t1.forward(x2-x1)
        t1.right(90)

def lab13():
    drawSquareWithFs()

def main():
    lab13()

if__name__=="__main__":
	main()