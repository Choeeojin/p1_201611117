alldata = [('content', 13.1, 37.1, 8.7, 1.5),
('method', 10.6, 34.6, 13.4, 1.9),
('strelation', 27.1, 40.0, 2.9, 1.5),
('prrelation', 16.2, 37.8, 6.8, 0.8),
('equipment', 11.4, 29.8, 14.8, 4.9),
('enviroment', 12.2, 26.5, 14.9, 4.4),
('subject', 13.5, 29.7, 11.1, 2.4),
('school', 13.7, 37.6, 4.1, 1.2)]

def data():
    best=list()
    for i in range(0,len(alldata)):
        best.append(alldata[i][1])
    good=list()
    for i in range(0,len(alldata)):
        good.append(alldata[i][2])
    bad=list()
    for i in range(0,len(alldata)):
        bad.append(alldata[i][3])
    worst=list()
    for i in range(0,len(alldata)):
        worst.append(alldata[i][4])
    sumb=0
    for i in range(0,len(alldata)):
        sumb = sumb + best[i]
    sumg = 0
    for i in range(0,len(alldata)):
        sumg = sumg + good[i]
    goodsum = 0
    goodsum = sumb + sumg
    print "Best and Good sum ", goodsum
    average = 0
    gaverage = goodsum / len(alldata)
    print "Best & Good average ", gaverage

    sumb=0
    for i in range(0,len(alldata)):
        sumb = sumb + bad[i]
    sumw=0
    for i in range(0,len(alldata)):
        sumw = sumw + worst[i]
    badsum = 0
    badsum = sumb + sumw
    print "Worst & Bad sum", badsum

    baverage = 0
    baverage = badsum / len(alldata)
    print "Worst & Bad average", baverage
    
def lab10():
    data()
def main():
    lab10()
    raw_input()
if __name__=="__main__":
    main()