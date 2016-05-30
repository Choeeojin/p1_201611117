data=[1,2,3,4,5,6,7,8,9,10]
fout=open('outputNumber.txt','w')
for i in data:
   if i%2==0:
     s='\n'
    else:
     s='\t'
    toPrint="{0}{1}".format(i,s)
    fout.write(toPrint)
fout.write('\n')

fout.close()