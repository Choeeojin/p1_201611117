﻿"""
@author cej
@since 160408
"""


mw=[(74425, 76326), (61164, 61636),(109688, 115744), (144796, 146776), (174996, 181676), (177841, 177434), (204630, 205980), (223373, 232245), (161055, 166130), (171576, 176735),(279169, 293772),(239450, 251066), (148690, 156510), (182977, 196992), (237792, 242641), (283869, 296762), (209344, 210282), (118965, 114441), (186503, 186856), (195734, 203014), (254381, 249472), (212401, 229111), (271654, 295354), (319197, 335045), (229829, 231671)]
m=0.
avm=0.
for i in range(0,len(mw)):
    m=m+mw[i][0]
print "all man ",m
avm = m / len(mw)
print "man avarage",avm

wm=0.
avwm=0.
for i in range(0,len(mw)):
    wm=wm+mw[i][1]
print "all woman ", wm
avwm= wm / len(mw)
print "woman average ", avwm


import matplotlib
import matplotlib.pyplot as plt

jongro=(74425,76326)
joongo=(61164 ,61636)
yungsan=(109688, 115744)
sungdong=(144796, 146776)
gwangjin=(174996, 181676)
dongda=(177841, 177434)
joongrang=(204630, 205980)
sungbuk=(223373, 232245)
gangbuk=(161055, 166130)
dobong=(171576, 176735)
nowon=(279169, 293772)
unpyeng=(239450, 251066)
sudamun=(148690, 156510)
mapo=(182977, 196992)
yangchun=(237792, 242641)
gangsu=(283869, 296762)
guro=(209344, 210282)
gumchun=(118965, 114441)
yongdunpo=(186503, 186856)
dongjak=(195734, 203014)
goanak=(254381, 249472)
sucho=(212401, 229111)
gangnam=(271654, 295354)
songpa=(319197, 335045)
gangdong=(229829, 231671)

gu={"jongro":jongro,"joongo":joongo,'yungsan':yungsan,'sungdong':sungdong,'gwangjin':gwangjin,'dongda':dongda,'joongrang':joongrang,'sungbuk':sungbuk,'gangbuk':gangbuk,'dobong':dobong,'nowon':nowon,'unpyeng':unpyeng,'unpyeng':unpyeng,'sudamun':sudamun,'mapo':mapo,'yangchun':yangchun,'gangsu':gangsu,'guro':guro,'gumchun':gumchun,'yongdunpo':yongdunpo,'dongjak':dongjak,'goanak':goanak,'sucho':sucho,'gangnam':gangnam,'songpa':songpa,'gangdong':gangdong}

d=dict()
for i in gu:
    d[str(i)]=gu[i][0]+gu[i][1]
plt.bar(range(len(d)),d.values(), align='center')
plt.xticks(range(len(d)), list(d.keys()))
plt.show()
