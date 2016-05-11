"""
@author cej
@since 160509
"""
alldata=list()
alldata=[["English",100,"Math",200],["English",200,"Math",200],["English",100,"Math",300]]
es=0
ms=0
for i in alldata:
    es=i[1]+es
    print es

for c in alldata:
    ms=c[3]+ms
    print ms
ea=es/len(alldata)
ma=ms/len(alldata)
print ea
print ma