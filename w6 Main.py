"""
@author cej
@since 160406
"""


begin=0
end=1000

def sumofMultiplesof3_5(begin,end):
    sum=0

    for i in range(begin,end):
        if i%3==0 or i%5==0:
            sum=sum+i
    print sum
    return sum


sumofMultiplesof3_5(1,1000)

def lab6():
	begin=0
	end=1000
	sumofMultiplesof3_5(1,1000)

def main():
	lab6()
if __name__=="__main__"
	main()