c = 1
while c == 1:
    a = list(str(input()))
    b = list(str(input()))
    s = ""
    for i in range(len(a)):
        a[i] = int(a[i])
        b[i] = int(b[i])
        if a[i] == 1:
            if b[i] == 2:
                s += "輸"
            elif b[i] == 5:
                s += "贏"
            else :
                s += "和"
        elif a[i] == 2:
            if b[i] == 3:
                s += "輸"
            elif b[i] == 1:
                s += "贏"
            else :
                s += "和"
        elif a[i] == 3:
            if b[i] == 4:
                s += "輸"
            elif b[i] == 2:
                s += "贏"
            else :
                s += "和"
        elif a[i] == 4:
            if b[i] == 5:
                s += "輸"
            elif b[i] == 3:
                s += "贏"
            else :
                s += "和"
        elif a[i] == 5:
            if b[i] == 1:
                s += "輸"
            elif b[i] == 4:
                s += "贏"
            else :
                s += "和"
        else:
            print("請輸入1到5的數字")
            c = 0
            break
    if c != 0:
        print(s)
        break
    else: c = 1