total = 0
while total == 0:
    a = list(map(str, input().split()))
    for i in range(len(a)):
        if a[i].isdigit() == True:
            if int(a[i]) > 1 and int(a[i]) < 11:
                a[i] = int(a[i])
            else:
                a[i] = 0
        elif a[i] == "A":
            a[i] = 1
        elif a[i] == "J":
            a[i] = 11
        elif a[i] == "Q":
            a[i] = 12
        elif a[i] == "K":
            a[i] = 13
        else:
            print("請輸入正確撲克點數")
            total = 0
            break
        total += a[i]
        if a[i] == 0:
            total = 0
            print("請輸入正確撲克點數")
            break
print(total)