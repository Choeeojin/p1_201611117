import os
mydir=os.getcwd()
filename='Square.txt'
myfile=open('Square.txt')
myfn=os.path.join(mydir,filename)
print myfile

%%writefile Square.txt
0,0,100,100
150,150,200,200

def getFsFromFile():
    fs=open('Square.txt','r')
    myfs=[]
    for line in fs:
        line1=line.split(',')
        aRect=[(line1[0],line1[1]),(line1[2],line1[3].strip())]
        myfs.append(aRect)
    fs.close()
    return fs

def lab13():
    getFsFromFile()

def main():
    lab13()

if__name__=="__main__":
	main()