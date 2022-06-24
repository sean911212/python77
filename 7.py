list1 = list(map(int, input("輸入月租費形式與通話時間為:").split(",")))
a = float(list1[0])
b = float(list1[1])
if a > b:
    print("通話費為:%d" %a)
elif a < b:
    if a == 186:
        if b <= a*2:
            print("通話費為:%d" % (round(round(b*0.09)*0.9)))
        else: print("通話費為:%d" %(round(round(b*0.09)*0.8)))
    elif a == 386:
        if b <= a*2:
            print("通話費為:%d" % (round(round(b*0.08)*0.8)))
        else: print("通話費為:%d" %(round(round(b*0.08)*0.7)))
    elif a == 586:
        if b <= a*2:
            print("通話費為:%d" % (round(round(b*0.07)*0.7)))
        else: print("通話費為:%d" %(round(round(b*0.07)*0.6)))
    elif a == 986:
        if b <= a*2:
            print("通話費為:%d" % (round(round(b*0.06)*0.6)))
        else: print("通話費為:%d" %(round(round(b*0.06)*0.5)))