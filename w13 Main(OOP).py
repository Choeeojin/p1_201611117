


class Dog(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        print "my dog name is ", self.name
    def talk(self):
        print "mung mung", self.name
        
class ShihTzu(Dog):
    def talk(self):
        print "si si", self.name

class Maltese(Dog):
    def talk(self):
        print "mal mal", self.name

def lab13():
    mydog1=Dog('Dog')
    mydog1.talk()

    mydog2=ShihTzu('ShihTzu')
    mydog2.talk()

    mydog3=Maltese('Maltese')
    mydog3.talk()

def main():
    lab13()
if __name__=="__main__":
    main()
