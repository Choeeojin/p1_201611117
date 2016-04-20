"""
@author cej
@since 160411
"""

d=list()

for i in range(0,1001):
    if i%4==0 and i%5>0:
        d.append(i)


def sumList(d):
    sum=0
    for j in range(0,len(d)):
        sum=sum+d[j]
    return sum
        

print sumList(d)

def lab6():
	mysum=sumList(d)
	print mysum

def main():
	lab6()

if __name__=="__main__":
	main()