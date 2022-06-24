a = list(map(int, input("輸入一整數列為:").split()))
c = 0
for i in range(len(a)):
    b = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            b += 1
    if b > len(a) // 2:
        c = a[i]
        break
if b > len(a) // 2:
    print("過半元素為%d" %c)
else: print("過半元素為:NO")