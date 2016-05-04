import math

Locations=list()
Locations=[(37.575821, 126.973580),(37.571601, 126.976687),(37.574604, 126.957676),(37.570134, 126.983015),(37.572531, 126.990492),(37.563642, 126.975296)]
lct=list()
for i in range(1,len(Locations)):
    Distances=math.sqrt((Locations[0][0]-Locations[i][0])**2+(Locations[0][1]-Locations[i][1])**2)
    print math.sqrt((Locations[0][0]-Locations[i][0])**2+(Locations[0][1]-Locations[i][1])**2)
    lct.append(Distances)
print lct
print min(lct)