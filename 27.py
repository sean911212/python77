while True:
    a = str(input("輸入整數列(end結束):"))
    if a == "end":
        print("結束")
        break
    a = list(a)
    list1 = []
    list2 = []
    for i in range(len(a) - 1):
        s = ""
        d = ""
        for j in range(i, len(a)):
            s += a[j]
            d = list(s)
            p = ""
            for k in range(len(d) - 1, -1, -1):
                p += d[k]
            if len(d) > 1: 
                if p == s:
                    list1.append(p)
                    list2.append(len(p))
        for i in range(len(list2) - 1, -1, -1):
            for j in range(len(list2) - 1, -1, -1):
                if list2[i] < list2[j]:
                    list2[i], list2[j] = list2[j], list2[i]
                    list1[i], list1[j] = list1[j], list1[i]
    max = list2[0]
    listMax = []
    for i in range(len(list2)):
        if list2[i] == max:
            listMax.append(list1[i])
    for i in range(len(listMax)):
        for j in range(len(listMax)):
            if int(listMax[i]) < int(listMax[j]):
                    listMax[i], listMax[j] = listMax[j], listMax[i]
    print("最長迴文數字子數列為:%s" %listMax[0])