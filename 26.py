while True:
    a = str(input("檢測的字串(end結束):"))
    if a == "end":
        break
    a = list(a)
    b = str(input("檢測的單一字元:"))
    c = 0
    for i in range(len(a)):
        if a[i] == b:
            c += 1
    print("字元%s出現的次數為:%d" %(b, c))