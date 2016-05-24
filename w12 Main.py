import os
mydir=os.getcwd()
print mydir
filename='python.txt'
myfilename=os.path.join(mydir,filename)
myfile='C:\Users\eojing\Desktop\\python.txt'
myfile=open(myfilename,'r')
contents=myfile.read()
for i in range(0,len(contents)):
    if contents[i].find('Python')>=0:
        print contents[i]
    else:
        print "Not found"
myfile.close()

myfile=open(myfilename,'r')
for line in myfile:
    if line.upper()=='LINE':
        print line
    else:
        print "Not found"
myfile.close()
