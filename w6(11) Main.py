"""
@author cej
@since 160406
"""


year=raw_input("Year? ")


def leapYear(year):
    if year%4==0 and not year%100==0:
        print year
    elif year%4==0 and year%400==0:
        print year
    else:
        print "error"






def lab6():
	year=raw_input("Year? ")
	leapYear(year)

def main():
	lab6()
if __name__=="__main__":
	main()