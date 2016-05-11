"""
@author cej
@since 160509
"""
coffee=list()
coffee=[["Coffee","Water","Milk","Icecream"]
  ,["Espresso","No","No","No"]
  ,["Long Black","Yes","No","No"]
  ,["Flat White","No","Yes","No"]
  ,["Cappuccino","No","Yes-Fronthy","No"]
  ,["Affogato","No","No","Yes"]]
data=coffee[1:len(coffee)]
print data
for i in data:
    if i[2].upper()=="YES":
        print i[0]

ms=0
nms=0
for i in data:
    if i[0]=="Flat White":
        i[2]=1
        ms=i[2]+ms
        print ms
    else:
        i[2]=1
        nms=i[2]+nms
print ms/(nms+ms)

