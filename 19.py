a = int(input("測試的資料量："))
for i in range(a):
    while True:
        b = list(map(str, input().split()))
        for i in range(len(b)):
            if b[i] == "O" or b[i] == "A" or b[i] == "B" or b[i] == "AB":
                c = 1
            else:
                c = 0
                break
        if c == 1:
            break
        else:
            print("請輸入正確血型(O, A, B, AB)")
    if b[0] == "O" and b[1] == "O":
        if b[2] != "O":
            print("IMPOSSIBLE")
        else:
            print("YES")
    elif b[0] == "O" or b[1] == "O":
        if b[0] == "A" or b[1] == "A":
            if b[2] != "O" and b[2] != "A":
                print("IMPOSSIBLE")
            else:
                print("YES")
        elif b[0] == "B" or b[1] == "B":
            if b[2] != "O" and b[2] != "B":
                print("IMPOSSIBLE")
            else:
                print("YES")
        elif b[0] == "AB" or b[1] == "AB":
            if b[2] != "A" and b[2] != "B":
                print("IMPOSSIBLE")
            else:
                print("YES")
    elif b[0] == "A" or b[1] == "A":
        if b[0] == "A" and b[1] == "A":
            if b[2] != "A" and b[2] != "O":
                print("IMPOSSIBLE")
            else:
                print("YES")
        elif b[0] == "B" or b[1] == "B":
            print("YES")
        elif b[0] == "AB" or b[1] == "AB":
            if b[2] != "A" and b[2] != "B" and b[2] != "AB":
                print("IMPOSSIBLE")
            else:
                print("YES")
    elif b[0] == "B" or b[1] == "B":
        if b[0] == "B" and b[1] == "B":
            if b[2] != "B" and b[2] != "O":
                print("IMPOSSIBLE")
            else:
                print("YES")
        elif b[0] == "AB" or b[1] == "AB":
            if b[2] != "A" and b[2] != "B" and b[2] != "AB":
                print("IMPOSSIBLE")
            else:
                print("YES")
    elif b[0] == "AB" or b[1] == "AB":
        if b[0] == "AB" and b[1] == "AB":
            if b[2] != "A" and b[2] != "B" and b[2] != "AB":
                print("IMPOSSIBLE")
            else:
                print("YES")