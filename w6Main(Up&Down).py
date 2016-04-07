"""
@author cej
@since 160408
"""



host=raw_input("Enter the number ")


def UpandDownGame():
    player=raw_input("Enter the number you think ")
    if host==player:
        print "Pass"
    elif host>player:
        print "Up"
        UpandDownGame()
    elif host<player:
        print "Down"
 	UpandDownGame()




def lab6():
	UpandDownGame()

def main():
	lab6()
if __name__=="__main__"
	main()